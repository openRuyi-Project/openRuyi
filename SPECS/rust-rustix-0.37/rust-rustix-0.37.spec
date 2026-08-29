# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rustix
%global full_version 0.37.28
%global pkgname rustix-0.37

Name:           rust-rustix-0.37
Version:        0.37.28
Release:        %autorelease
Summary:        Rust crate "rustix"
License:        Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
URL:            https://github.com/bytecodealliance/rustix
#!RemoteAsset:  sha256:519165d378b97752ca44bbe15047d5d3409e875f39327546b42ac81d7e18c1b6
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-1/default) >= 1.3.2
Requires:       crate(errno-0.3) >= 0.3.1
Requires:       crate(libc-0.2/default) >= 0.2.144
Requires:       crate(libc-0.2/extra-traits) >= 0.2.144
Requires:       crate(linux-raw-sys-0.3/errno) >= 0.3.6
Requires:       crate(linux-raw-sys-0.3/general) >= 0.3.6
Requires:       crate(linux-raw-sys-0.3/ioctl) >= 0.3.6
Requires:       crate(linux-raw-sys-0.3/no-std) >= 0.3.6
Requires:       crate(windows-sys-0.48/default) >= 0.48.0
Requires:       crate(windows-sys-0.48/win32-foundation) >= 0.48.0
Requires:       crate(windows-sys-0.48/win32-networking-winsock) >= 0.48.0
Requires:       crate(windows-sys-0.48/win32-networkmanagement-iphelper) >= 0.48.0
Requires:       crate(windows-sys-0.48/win32-system-threading) >= 0.48.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/core) = %{version}
Provides:       crate(%{pkgname}/fs) = %{version}
Provides:       crate(%{pkgname}/linux-4-11) = %{version}
Provides:       crate(%{pkgname}/linux-latest) = %{version}
Provides:       crate(%{pkgname}/mm) = %{version}
Provides:       crate(%{pkgname}/net) = %{version}
Provides:       crate(%{pkgname}/param) = %{version}
Provides:       crate(%{pkgname}/process) = %{version}
Provides:       crate(%{pkgname}/rand) = %{version}
Provides:       crate(%{pkgname}/runtime) = %{version}
Provides:       crate(%{pkgname}/termios) = %{version}
Provides:       crate(%{pkgname}/thread) = %{version}
Provides:       crate(%{pkgname}/time) = %{version}

%description
Source code for takopackized Rust crate "rustix"

%package     -n %{name}+all-apis
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock2-like syscalls - feature "all-apis"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/fs) = %{version}
Requires:       crate(%{pkgname}/io-uring) = %{version}
Requires:       crate(%{pkgname}/mm) = %{version}
Requires:       crate(%{pkgname}/net) = %{version}
Requires:       crate(%{pkgname}/param) = %{version}
Requires:       crate(%{pkgname}/process) = %{version}
Requires:       crate(%{pkgname}/procfs) = %{version}
Requires:       crate(%{pkgname}/pty) = %{version}
Requires:       crate(%{pkgname}/rand) = %{version}
Requires:       crate(%{pkgname}/runtime) = %{version}
Requires:       crate(%{pkgname}/termios) = %{version}
Requires:       crate(%{pkgname}/thread) = %{version}
Requires:       crate(%{pkgname}/time) = %{version}
Provides:       crate(%{pkgname}/all-apis) = %{version}

%description -n %{name}+all-apis
This metapackage enables feature "all-apis" for the Rust rustix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+all-impls
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock2-like syscalls - feature "all-impls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/fs-err) = %{version}
Requires:       crate(%{pkgname}/os-pipe) = %{version}
Provides:       crate(%{pkgname}/all-impls) = %{version}

%description -n %{name}+all-impls
This metapackage enables feature "all-impls" for the Rust rustix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cc
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock2-like syscalls - feature "cc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(cc-1/default) >= 1.0.68
Provides:       crate(%{pkgname}/cc) = %{version}

%description -n %{name}+cc
This metapackage enables feature "cc" for the Rust rustix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+compiler-builtins
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock2-like syscalls - feature "compiler_builtins"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(compiler-builtins-0.1/default) >= 0.1.49
Provides:       crate(%{pkgname}/compiler-builtins) = %{version}

%description -n %{name}+compiler-builtins
This metapackage enables feature "compiler_builtins" for the Rust rustix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock2-like syscalls - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/use-libc-auxv) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust rustix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+fs-err
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock2-like syscalls - feature "fs-err"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(io-lifetimes-1/close) >= 1.0.10
Requires:       crate(io-lifetimes-1/fs-err) >= 1.0.10
Provides:       crate(%{pkgname}/fs-err) = %{version}

%description -n %{name}+fs-err
This metapackage enables feature "fs-err" for the Rust rustix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+io-lifetimes
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock2-like syscalls - feature "io-lifetimes" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(io-lifetimes-1/close) >= 1.0.10
Provides:       crate(%{pkgname}/io-lifetimes) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+io-lifetimes
This metapackage enables feature "io-lifetimes" for the Rust rustix crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "std" feature.

%package     -n %{name}+io-uring
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock2-like syscalls - feature "io_uring"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/fs) = %{version}
Requires:       crate(%{pkgname}/net) = %{version}
Provides:       crate(%{pkgname}/io-uring) = %{version}

%description -n %{name}+io-uring
This metapackage enables feature "io_uring" for the Rust rustix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+itoa
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock2-like syscalls - feature "itoa"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(itoa-1) >= 1.0.1
Provides:       crate(%{pkgname}/itoa) = %{version}

%description -n %{name}+itoa
This metapackage enables feature "itoa" for the Rust rustix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libc
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock2-like syscalls - feature "libc" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libc-0.2/default) >= 0.2.144
Requires:       crate(libc-0.2/extra-traits) >= 0.2.144
Provides:       crate(%{pkgname}/libc) = %{version}
Provides:       crate(%{pkgname}/use-libc-auxv) = %{version}

%description -n %{name}+libc
This metapackage enables feature "libc" for the Rust rustix crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "use-libc-auxv" feature.

%package     -n %{name}+libc-errno
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock2-like syscalls - feature "libc_errno"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(errno-0.3) >= 0.3.1
Provides:       crate(%{pkgname}/libc-errno) = %{version}

%description -n %{name}+libc-errno
This metapackage enables feature "libc_errno" for the Rust rustix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+once-cell
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock2-like syscalls - feature "once_cell"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(once-cell-1/default) >= 1.5.2
Provides:       crate(%{pkgname}/once-cell) = %{version}

%description -n %{name}+once-cell
This metapackage enables feature "once_cell" for the Rust rustix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+os-pipe
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock2-like syscalls - feature "os_pipe"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(io-lifetimes-1/close) >= 1.0.10
Requires:       crate(io-lifetimes-1/os-pipe) >= 1.0.10
Provides:       crate(%{pkgname}/os-pipe) = %{version}

%description -n %{name}+os-pipe
This metapackage enables feature "os_pipe" for the Rust rustix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+procfs
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock2-like syscalls - feature "procfs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/fs) = %{version}
Requires:       crate(%{pkgname}/itoa) = %{version}
Requires:       crate(%{pkgname}/once-cell) = %{version}
Provides:       crate(%{pkgname}/procfs) = %{version}

%description -n %{name}+procfs
This metapackage enables feature "procfs" for the Rust rustix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pty
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock2-like syscalls - feature "pty"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/fs) = %{version}
Requires:       crate(%{pkgname}/itoa) = %{version}
Provides:       crate(%{pkgname}/pty) = %{version}

%description -n %{name}+pty
This metapackage enables feature "pty" for the Rust rustix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustc-dep-of-std
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock2-like syscalls - feature "rustc-dep-of-std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(%{pkgname}/compiler-builtins) = %{version}
Requires:       crate(%{pkgname}/core) = %{version}
Requires:       crate(bitflags-1/rustc-dep-of-std) >= 1.3.2
Requires:       crate(linux-raw-sys-0.3/errno) >= 0.3.6
Requires:       crate(linux-raw-sys-0.3/general) >= 0.3.6
Requires:       crate(linux-raw-sys-0.3/ioctl) >= 0.3.6
Requires:       crate(linux-raw-sys-0.3/no-std) >= 0.3.6
Requires:       crate(linux-raw-sys-0.3/rustc-dep-of-std) >= 0.3.6
Provides:       crate(%{pkgname}/rustc-dep-of-std) = %{version}

%description -n %{name}+rustc-dep-of-std
This metapackage enables feature "rustc-dep-of-std" for the Rust rustix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+use-libc
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock2-like syscalls - feature "use-libc"
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
