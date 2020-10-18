# Contributing to Change Journal


### Getting Started
This is mainly geared to [Codeprentice](https://github.com/codeprentice-org) members.
I added everyone who expressed interest in this project as repo collaborators:
* Khyber Sen (me)
* Saquib Shazad
* Asif Mallik
* Rickson Yang

This project is written in Rust, so if you're not familiar with Rust at all, 
look at the [Getting Started with Rust](#rust) section.

We're starting development on the [`fanotify`](#fanotify-on-linux) backend first,
so you should read that section and understand how the `fanotify` Linux API works first, 
especially with regards to `FAN_MARK_FILESYSTEM` and `FAN_MARK_MOUNT`.

Ideally, once we get the `fanotify` backend working for Linux, 
we'll also work on the USN Journal backend for Windows.
This'll probably be more complicated than the `fanotify` backend, 
since I haven't developed with Rust for Windows before, especially Windows APIs,
and there doesn't appear to be a good wrapper library for the USN Journal API
as there is for `fanotify`.

Then once that's done, we want to use this change journal library to create an 
[Everything](https://www.voidtools.com/)-like file searcher application.
Perhaps we can integrate it into [lolcate](https://github.com/ngirard/lolcate-rs),
a Rust file searcher that has a lot of nice features 
except for the real-time filesystem monitoring that Change Journal could provide.


#### Rust
To get started learning Rust, I really recommend the [Rust Book](https://doc.rust-lang.org/book/).
It's a really great introduction to Rust.  I'm not sure of other good learning materials, 
but you can always ask me any questions.


#### Fanotify on Linux
Most filesystem monitoring applications on Linux are built around 
the [`inotify`](https://man7.org/linux/man-pages/man7/inotify.7.html) API.
However, `inotify` is not recursive, so it can only watch a single directory at a time.
Thus, `inotify` doesn't work if you want to monitor large parts of or the whole filesystem.

Thus, more recently, Linux added 
the [`fanotify`](https://www.man7.org/linux/man-pages/man7/fanotify.7.html) API.
`fanotify` allows you to monitor the entire filesystem for file events.
This includes file creation/deletion/move events, which we're interested in, 
but also file access, open, close, modify, and attribute events.
Furthermore, the API allows you to read notifications of these events
as well as intercept them and influence the outcome of the event.
For example, you could intercept file open exec events and deny them if the file is a virus.
However, we're only interested in listening to file notification events for the change journal.

To understand the API better, I suggest reading:
* the overall [`fanotify` man page](https://www.man7.org/linux/man-pages/man7/fanotify.7.html)
* the [`fanotify_init` man page](https://www.man7.org/linux/man-pages/man2/fanotify_init.2.html)
* the [`fanotify_mark` man page](https://www.man7.org/linux/man-pages/man2/fanotify_mark.2.html)

Especially focus on the latter.

In the Rust world, there is already a crate, 
[file-descriptors](https://docs.rs/file-descriptors/0.9.1/file_descriptors/fanotify/struct.FanotifyFileDescriptor.html), 
that has an idiomatic Rust API around `fanotify`,
so I think we'll use that if it supports everything we need (it doesn't completely).
I also suggest reading how its API works and maps to the underlying `fanotify` Linux API.

Keep in mind that the entire `fanotify` API is not that new, but the parts required 
to use it for a change journal are fairly new (the last year or so, 2019-2020).
Because of this, there's not that much software using it in this way,
which is why I want to write this library.


#### NTFS USN Journal on Windows
On Windows, which uses NTFS, the filesystem maintains a journal of all file events
so that it can rollback things if the system crashes or is corrupted.
Besides it's own, internal journal of changes to make, 
it also maintains a change journal of changes that were made, 
and it exposes this to userspace for reading.

This is the Windows API that Everything (which is closed source) uses
for real-time file monitoring to keep an always up-to-date filesystem database.

We won't start working on the USN Journal backend until we finish the `fanotify` backend,
but for future reference, here is

* the [win32 documentation](https://docs.microsoft.com/en-us/windows/win32/fileio/change-journals)

and here are some Rust projects that use it, although none that I can find provide an idiomatic wrapper to it:
* [RustyUsn](https://github.com/forensicmatt/RustyUsn)
* [ddup](https://github.com/netaneld122/ddup)


#### Testing
Running tests for the USN Journal backend on Windows should be easy as long as you have a Windows machine.
The USN Journal API has multiple versions, but the API itself is pretty old, 
so I'm pretty sure it'll work on any non-ancient Windows version using NTFS. 

However, `fanotify`, and in particular the parts of the API that we need, are much newer.
We'll need to test on a Linux machine with a new enough Linux kernel (5.1).
This doesn't work on WSL on my machine, so we'll need a real Linux machine to test `fanotify`.
I think Ubuntu 18 and 20 use a new enough Linux kernel, but I'm not sure.
