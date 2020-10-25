use super::libc::*;

use bitflags::bitflags;

#[derive(Debug, Copy, Clone, Ord, PartialOrd, Eq, PartialEq, Hash)]
#[repr(u32)]
pub enum FanotifyNotificationClass {
    PreContent = FAN_CLASS_PRE_CONTENT as u32,
    Content = FAN_CLASS_CONTENT as u32,
    Notify = FAN_CLASS_NOTIF as u32,
}

impl Default for FanotifyNotificationClass {
    fn default() -> Self {
        Self::Notify
    }
}

bitflags! {
    pub struct FanotifyFlags: u32 {
        const CLOSE_ON_EXEC = FAN_CLOEXEC as u32;
        const NON_BLOCKING = FAN_NONBLOCK as u32;
        const UNLIMITED_QUEUE = FAN_UNLIMITED_QUEUE as u32;
        const UNLIMITED_MARKS = FAN_UNLIMITED_MARKS as u32;
        const REPORT_TID = FAN_REPORT_TID as u32;
        const REPORT_FID = FAN_REPORT_FID as u32;
        const REPORT_DIR_FID = FAN_REPORT_DIR_FID as u32;
        const REPORT_NAME = FAN_REPORT_NAME as u32;
    }
}

impl Default for FanotifyFlags {
    fn default() -> Self {
        Self::empty()
    }
}

impl FanotifyFlags {
    pub fn unlimited(self) -> Self {
        self | Self::UNLIMITED_QUEUE | Self::UNLIMITED_MARKS
    }
}

#[derive(Debug, Copy, Clone, Ord, PartialOrd, Eq, PartialEq, Hash)]
#[repr(u32)]
pub enum FanotifyReadWrite {
    Read = libc::O_RDONLY as u32,
    Write = libc::O_WRONLY as u32,
    ReadWrite = libc::O_RDWR as u32,
}

impl Default for FanotifyReadWrite {
    fn default() -> Self {
        Self::Read
    }
}

bitflags! {
    pub struct FanotifyEventFlags: u32 {
        const LARGE_FILE = libc::O_LARGEFILE as u32;
        const CLOSE_ON_EXEC = libc::O_CLOEXEC as u32;
        const APPEND = libc::O_APPEND as u32;
        const DATA_SYNC = libc::O_DSYNC as u32;
        const SYNC = libc::O_SYNC as u32;
        const NO_UPDATE_ACCESS_TIME = libc::O_NOATIME as u32;
        const NON_BLOCKING = libc::O_NONBLOCK as u32;
    }
}

impl Default for FanotifyEventFlags {
    fn default() -> Self {
        Self::empty()
    }
}
