# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rustix
%global full_version 1.1.4
%global pkgname rustix-1

Name:           rust-rustix-1
Version:        1.1.4
Release:        %autorelease
Summary:        Rust crate "rustix"
License:        Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
URL:            https://github.com/bytecodealliance/rustix
#!RemoteAsset:  sha256:b6fe4565b9518b83ef4f91bb47ce29620ca828bd32cb7e408f0062e9930ba190
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2) >= 2.4.0
Requires:       crate(errno-0.3) >= 0.3.10
Requires:       crate(libc-0.2) >= 0.2.182
Requires:       crate(linux-raw-sys-0.12/auxvec) >= 0.12.0
Requires:       crate(linux-raw-sys-0.12/elf) >= 0.12.0
Requires:       crate(linux-raw-sys-0.12/errno) >= 0.12.0
Requires:       crate(linux-raw-sys-0.12/general) >= 0.12.0
Requires:       crate(linux-raw-sys-0.12/ioctl) >= 0.12.0
Requires:       crate(linux-raw-sys-0.12/no-std) >= 0.12.0
Requires:       crate(windows-sys-0.52/default) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-foundation) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-networking-winsock) >= 0.52.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/core) = %{version}
Provides:       crate(%{pkgname}/event) = %{version}
Provides:       crate(%{pkgname}/fs) = %{version}
Provides:       crate(%{pkgname}/linux-4-11) = %{version}
Provides:       crate(%{pkgname}/linux-5-1) = %{version}
Provides:       crate(%{pkgname}/linux-5-11) = %{version}
Provides:       crate(%{pkgname}/linux-latest) = %{version}
Provides:       crate(%{pkgname}/mm) = %{version}
Provides:       crate(%{pkgname}/mount) = %{version}
Provides:       crate(%{pkgname}/param) = %{version}
Provides:       crate(%{pkgname}/pipe) = %{version}
Provides:       crate(%{pkgname}/pty) = %{version}
Provides:       crate(%{pkgname}/rand) = %{version}
Provides:       crate(%{pkgname}/rustc-std-workspace-alloc) = %{version}
Provides:       crate(%{pkgname}/shm) = %{version}
Provides:       crate(%{pkgname}/stdio) = %{version}
Provides:       crate(%{pkgname}/termios) = %{version}
Provides:       crate(%{pkgname}/time) = %{version}
Provides:       crate(%{pkgname}/try-close) = %{version}
Provides:       crate(%{pkgname}/use-explicitly-provided-auxv) = %{version}
Provides:       crate(%{pkgname}/use-libc-auxv) = %{version}

%description
Source code for takopackized Rust crate "rustix"

%package     -n %{name}+all-apis
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock-like syscalls - feature "all-apis"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/event) = %{version}
Requires:       crate(%{pkgname}/fs) = %{version}
Requires:       crate(%{pkgname}/io-uring) = %{version}
Requires:       crate(%{pkgname}/mm) = %{version}
Requires:       crate(%{pkgname}/mount) = %{version}
Requires:       crate(%{pkgname}/net) = %{version}
Requires:       crate(%{pkgname}/param) = %{version}
Requires:       crate(%{pkgname}/pipe) = %{version}
Requires:       crate(%{pkgname}/process) = %{version}
Requires:       crate(%{pkgname}/pty) = %{version}
Requires:       crate(%{pkgname}/rand) = %{version}
Requires:       crate(%{pkgname}/runtime) = %{version}
Requires:       crate(%{pkgname}/shm) = %{version}
Requires:       crate(%{pkgname}/stdio) = %{version}
Requires:       crate(%{pkgname}/system) = %{version}
Requires:       crate(%{pkgname}/termios) = %{version}
Requires:       crate(%{pkgname}/thread) = %{version}
Requires:       crate(%{pkgname}/time) = %{version}
Provides:       crate(%{pkgname}/all-apis) = %{version}

%description -n %{name}+all-apis
This metapackage enables feature "all-apis" for the Rust rustix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+io-uring
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock-like syscalls - feature "io_uring"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/event) = %{version}
Requires:       crate(%{pkgname}/fs) = %{version}
Requires:       crate(%{pkgname}/net) = %{version}
Requires:       crate(%{pkgname}/thread) = %{version}
Requires:       crate(linux-raw-sys-0.12/auxvec) >= 0.12.0
Requires:       crate(linux-raw-sys-0.12/elf) >= 0.12.0
Requires:       crate(linux-raw-sys-0.12/errno) >= 0.12.0
Requires:       crate(linux-raw-sys-0.12/general) >= 0.12.0
Requires:       crate(linux-raw-sys-0.12/io-uring) >= 0.12.0
Requires:       crate(linux-raw-sys-0.12/ioctl) >= 0.12.0
Requires:       crate(linux-raw-sys-0.12/no-std) >= 0.12.0
Provides:       crate(%{pkgname}/io-uring) = %{version}

%description -n %{name}+io-uring
This metapackage enables feature "io_uring" for the Rust rustix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libc
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock-like syscalls - feature "libc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libc-0.2) >= 0.2.182
Provides:       crate(%{pkgname}/libc) = %{version}

%description -n %{name}+libc
This metapackage enables feature "libc" for the Rust rustix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libc-errno
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock-like syscalls - feature "libc_errno"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(errno-0.3) >= 0.3.10
Provides:       crate(%{pkgname}/libc-errno) = %{version}

%description -n %{name}+libc-errno
This metapackage enables feature "libc_errno" for the Rust rustix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+net
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock-like syscalls - feature "net"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(linux-raw-sys-0.12/auxvec) >= 0.12.0
Requires:       crate(linux-raw-sys-0.12/elf) >= 0.12.0
Requires:       crate(linux-raw-sys-0.12/errno) >= 0.12.0
Requires:       crate(linux-raw-sys-0.12/general) >= 0.12.0
Requires:       crate(linux-raw-sys-0.12/if-ether) >= 0.12.0
Requires:       crate(linux-raw-sys-0.12/ioctl) >= 0.12.0
Requires:       crate(linux-raw-sys-0.12/net) >= 0.12.0
Requires:       crate(linux-raw-sys-0.12/netlink) >= 0.12.0
Requires:       crate(linux-raw-sys-0.12/no-std) >= 0.12.0
Requires:       crate(linux-raw-sys-0.12/xdp) >= 0.12.0
Provides:       crate(%{pkgname}/net) = %{version}

%description -n %{name}+net
This metapackage enables feature "net" for the Rust rustix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+process
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock-like syscalls - feature "process" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(linux-raw-sys-0.12/auxvec) >= 0.12.0
Requires:       crate(linux-raw-sys-0.12/elf) >= 0.12.0
Requires:       crate(linux-raw-sys-0.12/errno) >= 0.12.0
Requires:       crate(linux-raw-sys-0.12/general) >= 0.12.0
Requires:       crate(linux-raw-sys-0.12/ioctl) >= 0.12.0
Requires:       crate(linux-raw-sys-0.12/no-std) >= 0.12.0
Requires:       crate(linux-raw-sys-0.12/prctl) >= 0.12.0
Provides:       crate(%{pkgname}/process) = %{version}
Provides:       crate(%{pkgname}/runtime) = %{version}
Provides:       crate(%{pkgname}/thread) = %{version}

%description -n %{name}+process
This metapackage enables feature "process" for the Rust rustix crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "runtime", and "thread" features.

%package     -n %{name}+rustc-dep-of-std
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock-like syscalls - feature "rustc-dep-of-std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/core) = %{version}
Requires:       crate(%{pkgname}/rustc-std-workspace-alloc) = %{version}
Requires:       crate(bitflags-2/rustc-dep-of-std) >= 2.4.0
Requires:       crate(linux-raw-sys-0.12/auxvec) >= 0.12.0
Requires:       crate(linux-raw-sys-0.12/elf) >= 0.12.0
Requires:       crate(linux-raw-sys-0.12/errno) >= 0.12.0
Requires:       crate(linux-raw-sys-0.12/general) >= 0.12.0
Requires:       crate(linux-raw-sys-0.12/ioctl) >= 0.12.0
Requires:       crate(linux-raw-sys-0.12/no-std) >= 0.12.0
Requires:       crate(linux-raw-sys-0.12/rustc-dep-of-std) >= 0.12.0
Provides:       crate(%{pkgname}/rustc-dep-of-std) = %{version}

%description -n %{name}+rustc-dep-of-std
This metapackage enables feature "rustc-dep-of-std" for the Rust rustix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock-like syscalls - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(bitflags-2/std) >= 2.4.0
Requires:       crate(errno-0.3/std) >= 0.3.10
Requires:       crate(libc-0.2/std) >= 0.2.182
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust rustix crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+system
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock-like syscalls - feature "system"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(linux-raw-sys-0.12/auxvec) >= 0.12.0
Requires:       crate(linux-raw-sys-0.12/elf) >= 0.12.0
Requires:       crate(linux-raw-sys-0.12/errno) >= 0.12.0
Requires:       crate(linux-raw-sys-0.12/general) >= 0.12.0
Requires:       crate(linux-raw-sys-0.12/ioctl) >= 0.12.0
Requires:       crate(linux-raw-sys-0.12/no-std) >= 0.12.0
Requires:       crate(linux-raw-sys-0.12/system) >= 0.12.0
Provides:       crate(%{pkgname}/system) = %{version}

%description -n %{name}+system
This metapackage enables feature "system" for the Rust rustix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+use-libc
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock-like syscalls - feature "use-libc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/libc) = %{version}
Requires:       crate(%{pkgname}/libc-errno) = %{version}
Provides:       crate(%{pkgname}/use-libc) = %{version}

%description -n %{name}+use-libc
This metapackage enables feature "use-libc" for the Rust rustix crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
