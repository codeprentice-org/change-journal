# Change Journal

This library provides a unified change journal-like API for Linux and Windows.
That is, it lets you monitor entire filesystems, mount points, and/or volumes 
for file change events.

On Linux, it uses the [`fanotify`](https://www.man7.org/linux/man-pages/man7/fanotify.7.html) API.

On Windows, it uses the [USN Journal](https://docs.microsoft.com/en-us/windows/win32/fileio/change-journals) API.


Currently, neither backend is supported. 
The Linux `fanotify` backend will be added first, 
then the Windows USN Journal backend next.


## Permissions
On Linux, using `fanotify` requires the `CAP_SYS_ADMIN` permission (i.e. `sudo`).

On Windows, reading the USN Journal requires administrator privileges.


## Supported OSes
`fanotify` is required on Linux, which was added in Linux kernel version 2.6.37.
However, many useful `fanotify` operations were only added in Linux kernel version 5.1.

The NTFS USN Journal has been on Windows for a very long time, since Windows 7 at least I believe.
There shouldn't be any issues with Windows version for this.

macOS is not currently supported, mainly because the real-time file searcher functionality
this library can enable is already fulfilled very well by Spotlight.


## Roadmap
- [ ] Implement the `fanotify` backend from scratch 
      in the [fanotify](https://github.com/codeprentice-org/fanotify) crate
      using [libc](https://github.com/rust-lang/libc) bindings.

- [ ] Implement the USN Journal backend from scratch 
      in the [usn-journal](https://github.com/codeprentice-org/usn-journal) crate
      using [windows](https://github.com/microsoft/windows-rs) bindings.

- [ ] Integrate with a file searcher program like [lolcate](https://github.com/ngirard/lolcate-rs)
      to provide real-time filesystem monitoring so that no slow, manual indexing has to be performed.


## Progress

### Fall 2020
One paragraph describing the project and what was the initial plan

One paragraph summarizing what the team learnt in the process of the project, the difficulties faced and progress made (or not made)

The Change Journal project aims to create idiomatic Rust crates (libraries) 
that provide a cross-platform change journal-like API. 
That is, it lets you monitor entire filesystems, mount points, and/or volumes for file change or access events.
Essentially, it lets you query a filesystem journal for file events as they occur.

This project is split into multiple crates.  
First, there are OS-specific crates that provide low-level (but safe and idiomatic) access
to that OS's change journal-like API.

* On Linux, there is the [`fanotify`](https://github.com/codeprentice-org/fanotify) crate,
which uses Linux's [`fanotify`](https://www.man7.org/linux/man-pages/man7/fanotify.7.html) API.

* On Windows, there is the [`usn-journal`](https://github.com/codeprentice-org/usn-journal) crate,
which uses Windows' [USN Journal](https://docs.microsoft.com/en-us/windows/win32/fileio/change-journals) API.

Then there is the [`change-journal`](https://github.com/codeprentice-org/change-journal) crate,
which provides a cross-platform API on top of these platform-specific backends.

This fall of 2020, we started the implementation of the [`fanotify`](https://github.com/codeprentice-org/fanotify) crate.
There were some existing crates that offered some `fanotify` API, 
but they were generally unsafe, incomplete, and/or unidiomatic.
Thus, we decided to create our own `fanotify` library from scratch, using only the raw `libc` bindings.
So far, we have developed a thorough and very idiomatic API that encompasses the entire `fanotify` API.
Though it necessarily uses `unsafe` at the FFI-boundary, 
it exposes a completely safe public API.

A lot of time was spent making sure this API was as idiomatic and safe as possible 
without incurring significant extra runtime costs, 
since this is meant to be a very low-level library.
For example, when file events are read from a `Fanotify` struct,
we wanted to return an `Iterator` over `Event`s.
However, at the same time, we wanted to allow the user to be able 
to supply a pre-allocated buffer to avoid repeated allocations.
Furthermore, some events are permission events, meaning they require the `fanotify` user
to write back a permission decision to the `fanotify` file descriptor
to tell the OS to allow or deny a certain file event (very useful for antivirus software, for example).
We also wanted to make it impossible for the user to forget to write the decision back,
and make it as easy as marking the `FilePermission` struct with `permission.decision = Deny;`.
And to avoid excessive, small writes, we wanted to batch writes together as well.
Creating an API that offered all of this 
while still following Rust's rules for ownership, mutability, and lifetimes was very difficult, 
but we eventually managed to do so with only a very minor runtime overhead.
The end result is an idiomatic API that is very hard to misuse 
and has the necessary escape hatches for performance optimization when needed.

Since completing the `fanotify` API, we have spent our time writing more thorough documentation for the crate,
and now in extensive testing to ensure the `fanotify` crate works in all sorts of cases, 
from normal file events on `ext4` to in-memory filesystems like `tmpfs`,
as well network filesystems like `nfs` or pseudo filesystems like `procfs`.

We hope to publish our first official release to [crates.io](`https://crates.io/crates/fanotify`) very soon,
once we have finished adding more thorough testing.
