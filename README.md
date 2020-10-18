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
- [ ] Implement the `fanotify` backend using 
the [file-descriptors](https://docs.rs/file-descriptors/0.9.1/file_descriptors/fanotify/struct.FanotifyFileDescriptor.html) crate.

- [ ] Implement the USN Journal backend.

- [ ] Integrate with a file searcher program like [lolcate](https://github.com/ngirard/lolcate-rs)
      to provide real-time filesystem monitoring so that no slow, manual indexing has to be performed.
