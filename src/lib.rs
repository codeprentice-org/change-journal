pub mod fanotify;

#[cfg(test)]
mod tests {
    use crate::fanotify::descriptor::{FanotifyInit, FanotifyError};
    use std::error::Error;

    #[test]
    fn it_works() {
        let args = FanotifyInit {
            ..Default::default()
        };
        match args.run() {
            Ok(fd) => {

            },
            Err(e) => {
                assert_eq!(e, FanotifyError::Unsupported);
            }
        }
        assert_eq!(2 + 2, 4);
    }
}
