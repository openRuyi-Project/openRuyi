# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rustix
%global full_version 0.38.44
%global pkgname rustix-0.38

Name:           rust-rustix-0.38
Version:        0.38.44
Release:        %autorelease
Summary:        Rust crate "rustix"
License:        Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
URL:            https://github.com/bytecodealliance/rustix
#!RemoteAsset:  sha256:fdb5bc1ae2baa591800df16c9ca78619bf65c0488b41b96ccec5d11220d8c154
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2) >= 2.4.0
Requires:       crate(errno-0.3) >= 0.3.10
Requires:       crate(libc-0.2) >= 0.2.161
Requires:       crate(linux-raw-sys-0.4/elf) >= 0.4.14
Requires:       crate(linux-raw-sys-0.4/errno) >= 0.4.14
Requires:       crate(linux-raw-sys-0.4/general) >= 0.4.14
Requires:       crate(linux-raw-sys-0.4/ioctl) >= 0.4.14
Requires:       crate(linux-raw-sys-0.4/no-std) >= 0.4.14
Requires:       crate(windows-sys-0.52/default) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-foundation) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-networking-winsock) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-networkmanagement-iphelper) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-system-threading) >= 0.52.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/cc) = %{version}
Provides:       crate(%{pkgname}/core) = %{version}
Provides:       crate(%{pkgname}/event) = %{version}
Provides:       crate(%{pkgname}/fs) = %{version}
Provides:       crate(%{pkgname}/linux-4-11) = %{version}
Provides:       crate(%{pkgname}/linux-latest) = %{version}
Provides:       crate(%{pkgname}/mm) = %{version}
Provides:       crate(%{pkgname}/mount) = %{version}
Provides:       crate(%{pkgname}/param) = %{version}
Provides:       crate(%{pkgname}/pipe) = %{version}
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
Requires:       crate(%{pkgname}/procfs) = %{version}
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

%package     -n %{name}+compiler-builtins
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock-like syscalls - feature "compiler_builtins"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(compiler-builtins-0.1/default) >= 0.1.49
Provides:       crate(%{pkgname}/compiler-builtins) = %{version}

%description -n %{name}+compiler-builtins
This metapackage enables feature "compiler_builtins" for the Rust rustix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock-like syscalls - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/use-libc-auxv) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust rustix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+io-uring
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock-like syscalls - feature "io_uring"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/event) = %{version}
Requires:       crate(%{pkgname}/fs) = %{version}
Requires:       crate(%{pkgname}/net) = %{version}
Requires:       crate(linux-raw-sys-0.4/elf) >= 0.4.14
Requires:       crate(linux-raw-sys-0.4/errno) >= 0.4.14
Requires:       crate(linux-raw-sys-0.4/general) >= 0.4.14
Requires:       crate(linux-raw-sys-0.4/io-uring) >= 0.4.14
Requires:       crate(linux-raw-sys-0.4/ioctl) >= 0.4.14
Requires:       crate(linux-raw-sys-0.4/no-std) >= 0.4.14
Provides:       crate(%{pkgname}/io-uring) = %{version}

%description -n %{name}+io-uring
This metapackage enables feature "io_uring" for the Rust rustix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+itoa
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock-like syscalls - feature "itoa"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(itoa-1) >= 1.0.13
Provides:       crate(%{pkgname}/itoa) = %{version}

%description -n %{name}+itoa
This metapackage enables feature "itoa" for the Rust rustix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libc
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock-like syscalls - feature "libc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libc-0.2) >= 0.2.161
Provides:       crate(%{pkgname}/libc) = %{version}

%description -n %{name}+libc
This metapackage enables feature "libc" for the Rust rustix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libc-extra-traits
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock-like syscalls - feature "libc-extra-traits"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libc-0.2/extra-traits) >= 0.2.161
Provides:       crate(%{pkgname}/libc-extra-traits) = %{version}

%description -n %{name}+libc-extra-traits
This metapackage enables feature "libc-extra-traits" for the Rust rustix crate, by pulling in any additional dependencies needed by that feature.

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
Requires:       crate(linux-raw-sys-0.4/elf) >= 0.4.14
Requires:       crate(linux-raw-sys-0.4/errno) >= 0.4.14
Requires:       crate(linux-raw-sys-0.4/general) >= 0.4.14
Requires:       crate(linux-raw-sys-0.4/if-ether) >= 0.4.14
Requires:       crate(linux-raw-sys-0.4/ioctl) >= 0.4.14
Requires:       crate(linux-raw-sys-0.4/net) >= 0.4.14
Requires:       crate(linux-raw-sys-0.4/netlink) >= 0.4.14
Requires:       crate(linux-raw-sys-0.4/no-std) >= 0.4.14
Requires:       crate(linux-raw-sys-0.4/xdp) >= 0.4.14
Provides:       crate(%{pkgname}/net) = %{version}

%description -n %{name}+net
This metapackage enables feature "net" for the Rust rustix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+once-cell
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock-like syscalls - feature "once_cell"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(once-cell-1/default) >= 1.5.2
Provides:       crate(%{pkgname}/once-cell) = %{version}

%description -n %{name}+once-cell
This metapackage enables feature "once_cell" for the Rust rustix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+process
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock-like syscalls - feature "process" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(linux-raw-sys-0.4/elf) >= 0.4.14
Requires:       crate(linux-raw-sys-0.4/errno) >= 0.4.14
Requires:       crate(linux-raw-sys-0.4/general) >= 0.4.14
Requires:       crate(linux-raw-sys-0.4/ioctl) >= 0.4.14
Requires:       crate(linux-raw-sys-0.4/no-std) >= 0.4.14
Requires:       crate(linux-raw-sys-0.4/prctl) >= 0.4.14
Provides:       crate(%{pkgname}/process) = %{version}
Provides:       crate(%{pkgname}/runtime) = %{version}
Provides:       crate(%{pkgname}/thread) = %{version}

%description -n %{name}+process
This metapackage enables feature "process" for the Rust rustix crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "runtime", and "thread" features.

%package     -n %{name}+procfs
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock-like syscalls - feature "procfs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/fs) = %{version}
Requires:       crate(%{pkgname}/itoa) = %{version}
Requires:       crate(%{pkgname}/once-cell) = %{version}
Provides:       crate(%{pkgname}/procfs) = %{version}

%description -n %{name}+procfs
This metapackage enables feature "procfs" for the Rust rustix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pty
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock-like syscalls - feature "pty"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/fs) = %{version}
Requires:       crate(%{pkgname}/itoa) = %{version}
Provides:       crate(%{pkgname}/pty) = %{version}

%description -n %{name}+pty
This metapackage enables feature "pty" for the Rust rustix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustc-dep-of-std
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock-like syscalls - feature "rustc-dep-of-std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/compiler-builtins) = %{version}
Requires:       crate(%{pkgname}/core) = %{version}
Requires:       crate(%{pkgname}/rustc-std-workspace-alloc) = %{version}
Requires:       crate(bitflags-2/rustc-dep-of-std) >= 2.4.0
Requires:       crate(compiler-builtins-0.1/rustc-dep-of-std) >= 0.1.49
Requires:       crate(linux-raw-sys-0.4/elf) >= 0.4.14
Requires:       crate(linux-raw-sys-0.4/errno) >= 0.4.14
Requires:       crate(linux-raw-sys-0.4/general) >= 0.4.14
Requires:       crate(linux-raw-sys-0.4/ioctl) >= 0.4.14
Requires:       crate(linux-raw-sys-0.4/no-std) >= 0.4.14
Requires:       crate(linux-raw-sys-0.4/rustc-dep-of-std) >= 0.4.14
Provides:       crate(%{pkgname}/rustc-dep-of-std) = %{version}

%description -n %{name}+rustc-dep-of-std
This metapackage enables feature "rustc-dep-of-std" for the Rust rustix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock-like syscalls - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(%{pkgname}/libc-extra-traits) = %{version}
Requires:       crate(bitflags-2/std) >= 2.4.0
Requires:       crate(errno-0.3/std) >= 0.3.10
Requires:       crate(libc-0.2/std) >= 0.2.161
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust rustix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+system
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock-like syscalls - feature "system"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(linux-raw-sys-0.4/elf) >= 0.4.14
Requires:       crate(linux-raw-sys-0.4/errno) >= 0.4.14
Requires:       crate(linux-raw-sys-0.4/general) >= 0.4.14
Requires:       crate(linux-raw-sys-0.4/ioctl) >= 0.4.14
Requires:       crate(linux-raw-sys-0.4/no-std) >= 0.4.14
Requires:       crate(linux-raw-sys-0.4/system) >= 0.4.14
Provides:       crate(%{pkgname}/system) = %{version}

%description -n %{name}+system
This metapackage enables feature "system" for the Rust rustix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+use-libc
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock-like syscalls - feature "use-libc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/libc) = %{version}
Requires:       crate(%{pkgname}/libc-errno) = %{version}
Requires:       crate(%{pkgname}/libc-extra-traits) = %{version}
Provides:       crate(%{pkgname}/use-libc) = %{version}

%description -n %{name}+use-libc
This metapackage enables feature "use-libc" for the Rust rustix crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
