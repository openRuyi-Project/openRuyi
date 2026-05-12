# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rustix
%global full_version 1.1.4
%global pkgname rustix-1.0

Name:           rust-rustix-1.0
Version:        1.1.4
Release:        %autorelease
Summary:        Rust crate "rustix"
License:        Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
URL:            https://github.com/bytecodealliance/rustix
#!RemoteAsset:  sha256:b6fe4565b9518b83ef4f91bb47ce29620ca828bd32cb7e408f0062e9930ba190
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2.0) >= 2.11.0
Requires:       crate(errno-0.3) >= 0.3.14
Requires:       crate(libc-0.2) >= 0.2.183
Requires:       crate(linux-raw-sys-0.12/auxvec) >= 0.12.1
Requires:       crate(linux-raw-sys-0.12/elf) >= 0.12.1
Requires:       crate(linux-raw-sys-0.12/errno) >= 0.12.1
Requires:       crate(linux-raw-sys-0.12/general) >= 0.12.1
Requires:       crate(linux-raw-sys-0.12/ioctl) >= 0.12.1
Requires:       crate(linux-raw-sys-0.12/no-std) >= 0.12.1
Requires:       crate(windows-sys-0.61/default) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-foundation) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-networking-winsock) >= 0.61.2
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/event)
Provides:       crate(%{pkgname}/fs)
Provides:       crate(%{pkgname}/linux-4-11)
Provides:       crate(%{pkgname}/linux-5-1)
Provides:       crate(%{pkgname}/linux-5-11)
Provides:       crate(%{pkgname}/linux-latest)
Provides:       crate(%{pkgname}/mm)
Provides:       crate(%{pkgname}/mount)
Provides:       crate(%{pkgname}/param)
Provides:       crate(%{pkgname}/pipe)
Provides:       crate(%{pkgname}/pty)
Provides:       crate(%{pkgname}/rand)
Provides:       crate(%{pkgname}/shm)
Provides:       crate(%{pkgname}/stdio)
Provides:       crate(%{pkgname}/termios)
Provides:       crate(%{pkgname}/time)
Provides:       crate(%{pkgname}/try-close)
Provides:       crate(%{pkgname}/use-explicitly-provided-auxv)
Provides:       crate(%{pkgname}/use-libc-auxv)

%description
Source code for takopackized Rust crate "rustix"

%package     -n %{name}+all-apis
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock-like syscalls - feature "all-apis"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/event)
Requires:       crate(%{pkgname}/fs)
Requires:       crate(%{pkgname}/io-uring)
Requires:       crate(%{pkgname}/mm)
Requires:       crate(%{pkgname}/mount)
Requires:       crate(%{pkgname}/net)
Requires:       crate(%{pkgname}/param)
Requires:       crate(%{pkgname}/pipe)
Requires:       crate(%{pkgname}/process)
Requires:       crate(%{pkgname}/pty)
Requires:       crate(%{pkgname}/rand)
Requires:       crate(%{pkgname}/runtime)
Requires:       crate(%{pkgname}/shm)
Requires:       crate(%{pkgname}/stdio)
Requires:       crate(%{pkgname}/system)
Requires:       crate(%{pkgname}/termios)
Requires:       crate(%{pkgname}/thread)
Requires:       crate(%{pkgname}/time)
Provides:       crate(%{pkgname}/all-apis)

%description -n %{name}+all-apis
This metapackage enables feature "all-apis" for the Rust rustix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+core
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock-like syscalls - feature "core"
Requires:       crate(%{pkgname})
Requires:       crate(rustc-std-workspace-core-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/core)

%description -n %{name}+core
This metapackage enables feature "core" for the Rust rustix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+io-uring
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock-like syscalls - feature "io_uring"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/event)
Requires:       crate(%{pkgname}/fs)
Requires:       crate(%{pkgname}/net)
Requires:       crate(%{pkgname}/thread)
Requires:       crate(linux-raw-sys-0.12/auxvec) >= 0.12.1
Requires:       crate(linux-raw-sys-0.12/elf) >= 0.12.1
Requires:       crate(linux-raw-sys-0.12/errno) >= 0.12.1
Requires:       crate(linux-raw-sys-0.12/general) >= 0.12.1
Requires:       crate(linux-raw-sys-0.12/io-uring) >= 0.12.1
Requires:       crate(linux-raw-sys-0.12/ioctl) >= 0.12.1
Requires:       crate(linux-raw-sys-0.12/no-std) >= 0.12.1
Provides:       crate(%{pkgname}/io-uring)

%description -n %{name}+io-uring
This metapackage enables feature "io_uring" for the Rust rustix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libc
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock-like syscalls - feature "libc"
Requires:       crate(%{pkgname})
Requires:       crate(libc-0.2) >= 0.2.183
Provides:       crate(%{pkgname}/libc)

%description -n %{name}+libc
This metapackage enables feature "libc" for the Rust rustix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libc-errno
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock-like syscalls - feature "libc_errno"
Requires:       crate(%{pkgname})
Requires:       crate(errno-0.3) >= 0.3.14
Provides:       crate(%{pkgname}/libc-errno)

%description -n %{name}+libc-errno
This metapackage enables feature "libc_errno" for the Rust rustix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+net
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock-like syscalls - feature "net"
Requires:       crate(%{pkgname})
Requires:       crate(linux-raw-sys-0.12/auxvec) >= 0.12.1
Requires:       crate(linux-raw-sys-0.12/elf) >= 0.12.1
Requires:       crate(linux-raw-sys-0.12/errno) >= 0.12.1
Requires:       crate(linux-raw-sys-0.12/general) >= 0.12.1
Requires:       crate(linux-raw-sys-0.12/if-ether) >= 0.12.1
Requires:       crate(linux-raw-sys-0.12/ioctl) >= 0.12.1
Requires:       crate(linux-raw-sys-0.12/net) >= 0.12.1
Requires:       crate(linux-raw-sys-0.12/netlink) >= 0.12.1
Requires:       crate(linux-raw-sys-0.12/no-std) >= 0.12.1
Requires:       crate(linux-raw-sys-0.12/xdp) >= 0.12.1
Provides:       crate(%{pkgname}/net)

%description -n %{name}+net
This metapackage enables feature "net" for the Rust rustix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+process
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock-like syscalls - feature "process" and 2 more
Requires:       crate(%{pkgname})
Requires:       crate(linux-raw-sys-0.12/auxvec) >= 0.12.1
Requires:       crate(linux-raw-sys-0.12/elf) >= 0.12.1
Requires:       crate(linux-raw-sys-0.12/errno) >= 0.12.1
Requires:       crate(linux-raw-sys-0.12/general) >= 0.12.1
Requires:       crate(linux-raw-sys-0.12/ioctl) >= 0.12.1
Requires:       crate(linux-raw-sys-0.12/no-std) >= 0.12.1
Requires:       crate(linux-raw-sys-0.12/prctl) >= 0.12.1
Provides:       crate(%{pkgname}/process)
Provides:       crate(%{pkgname}/runtime)
Provides:       crate(%{pkgname}/thread)

%description -n %{name}+process
This metapackage enables feature "process" for the Rust rustix crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "runtime", and "thread" features.

%package     -n %{name}+rustc-dep-of-std
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock-like syscalls - feature "rustc-dep-of-std"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/core)
Requires:       crate(%{pkgname}/rustc-std-workspace-alloc)
Requires:       crate(bitflags-2.0/rustc-dep-of-std) >= 2.11.0
Requires:       crate(linux-raw-sys-0.12/auxvec) >= 0.12.1
Requires:       crate(linux-raw-sys-0.12/elf) >= 0.12.1
Requires:       crate(linux-raw-sys-0.12/errno) >= 0.12.1
Requires:       crate(linux-raw-sys-0.12/general) >= 0.12.1
Requires:       crate(linux-raw-sys-0.12/ioctl) >= 0.12.1
Requires:       crate(linux-raw-sys-0.12/no-std) >= 0.12.1
Requires:       crate(linux-raw-sys-0.12/rustc-dep-of-std) >= 0.12.1
Provides:       crate(%{pkgname}/rustc-dep-of-std)

%description -n %{name}+rustc-dep-of-std
This metapackage enables feature "rustc-dep-of-std" for the Rust rustix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustc-std-workspace-alloc
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock-like syscalls - feature "rustc-std-workspace-alloc"
Requires:       crate(%{pkgname})
Requires:       crate(rustc-std-workspace-alloc-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/rustc-std-workspace-alloc)

%description -n %{name}+rustc-std-workspace-alloc
This metapackage enables feature "rustc-std-workspace-alloc" for the Rust rustix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock-like syscalls - feature "std" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(bitflags-2.0/std) >= 2.11.0
Requires:       crate(errno-0.3/std) >= 0.3.14
Requires:       crate(libc-0.2/std) >= 0.2.183
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust rustix crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+system
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock-like syscalls - feature "system"
Requires:       crate(%{pkgname})
Requires:       crate(linux-raw-sys-0.12/auxvec) >= 0.12.1
Requires:       crate(linux-raw-sys-0.12/elf) >= 0.12.1
Requires:       crate(linux-raw-sys-0.12/errno) >= 0.12.1
Requires:       crate(linux-raw-sys-0.12/general) >= 0.12.1
Requires:       crate(linux-raw-sys-0.12/ioctl) >= 0.12.1
Requires:       crate(linux-raw-sys-0.12/no-std) >= 0.12.1
Requires:       crate(linux-raw-sys-0.12/system) >= 0.12.1
Provides:       crate(%{pkgname}/system)

%description -n %{name}+system
This metapackage enables feature "system" for the Rust rustix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+use-libc
Summary:        Safe Rust bindings to POSIX/Unix/Linux/Winsock-like syscalls - feature "use-libc"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/libc)
Requires:       crate(%{pkgname}/libc-errno)
Provides:       crate(%{pkgname}/use-libc)

%description -n %{name}+use-libc
This metapackage enables feature "use-libc" for the Rust rustix crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
