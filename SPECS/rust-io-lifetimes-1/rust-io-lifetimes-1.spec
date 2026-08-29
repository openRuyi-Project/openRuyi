# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name io-lifetimes
%global full_version 1.0.11
%global pkgname io-lifetimes-1

Name:           rust-io-lifetimes-1
Version:        1.0.11
Release:        %autorelease
Summary:        Rust crate "io-lifetimes"
License:        Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
URL:            https://github.com/sunfishcode/io-lifetimes
#!RemoteAsset:  sha256:eae7b9aee968036d54dce06cebaefd919e4472e753296daccd6d344e3e2df0c2
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "io-lifetimes"

%package     -n %{name}+async-std
Summary:        Low-level I/O ownership and borrowing library - feature "async-std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(async-std-1/default) >= 1.12.0
Provides:       crate(%{pkgname}/async-std) = %{version}

%description -n %{name}+async-std
This metapackage enables feature "async-std" for the Rust io-lifetimes crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+close
Summary:        Low-level I/O ownership and borrowing library - feature "close" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/hermit-abi) = %{version}
Requires:       crate(%{pkgname}/libc) = %{version}
Requires:       crate(%{pkgname}/windows-sys) = %{version}
Provides:       crate(%{pkgname}/close) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+close
This metapackage enables feature "close" for the Rust io-lifetimes crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+fs-err
Summary:        Low-level I/O ownership and borrowing library - feature "fs-err"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(fs-err-2/default) >= 2.6.0
Provides:       crate(%{pkgname}/fs-err) = %{version}

%description -n %{name}+fs-err
This metapackage enables feature "fs-err" for the Rust io-lifetimes crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+hermit-abi
Summary:        Low-level I/O ownership and borrowing library - feature "hermit-abi"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hermit-abi-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/hermit-abi) = %{version}

%description -n %{name}+hermit-abi
This metapackage enables feature "hermit-abi" for the Rust io-lifetimes crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libc
Summary:        Low-level I/O ownership and borrowing library - feature "libc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libc-0.2/default) >= 0.2.96
Provides:       crate(%{pkgname}/libc) = %{version}

%description -n %{name}+libc
This metapackage enables feature "libc" for the Rust io-lifetimes crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mio
Summary:        Low-level I/O ownership and borrowing library - feature "mio"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(mio-0.8/default) >= 0.8.0
Requires:       crate(mio-0.8/net) >= 0.8.0
Requires:       crate(mio-0.8/os-ext) >= 0.8.0
Provides:       crate(%{pkgname}/mio) = %{version}

%description -n %{name}+mio
This metapackage enables feature "mio" for the Rust io-lifetimes crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+os-pipe
Summary:        Low-level I/O ownership and borrowing library - feature "os_pipe"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(os-pipe-1/default) >= 1.0.0
Requires:       crate(os-pipe-1/io-safety) >= 1.0.0
Provides:       crate(%{pkgname}/os-pipe) = %{version}

%description -n %{name}+os-pipe
This metapackage enables feature "os_pipe" for the Rust io-lifetimes crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+socket2
Summary:        Low-level I/O ownership and borrowing library - feature "socket2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(socket2-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/socket2) = %{version}

%description -n %{name}+socket2
This metapackage enables feature "socket2" for the Rust io-lifetimes crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio
Summary:        Low-level I/O ownership and borrowing library - feature "tokio"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-1/default) >= 1.6.0
Requires:       crate(tokio-1/fs) >= 1.6.0
Requires:       crate(tokio-1/io-std) >= 1.6.0
Requires:       crate(tokio-1/net) >= 1.6.0
Requires:       crate(tokio-1/process) >= 1.6.0
Provides:       crate(%{pkgname}/tokio) = %{version}

%description -n %{name}+tokio
This metapackage enables feature "tokio" for the Rust io-lifetimes crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+windows-sys
Summary:        Low-level I/O ownership and borrowing library - feature "windows-sys"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(windows-sys-0.48/default) >= 0.48.0
Requires:       crate(windows-sys-0.48/win32-foundation) >= 0.48.0
Requires:       crate(windows-sys-0.48/win32-networking-winsock) >= 0.48.0
Requires:       crate(windows-sys-0.48/win32-security) >= 0.48.0
Requires:       crate(windows-sys-0.48/win32-storage-filesystem) >= 0.48.0
Requires:       crate(windows-sys-0.48/win32-system-io) >= 0.48.0
Requires:       crate(windows-sys-0.48/win32-system-threading) >= 0.48.0
Provides:       crate(%{pkgname}/windows-sys) = %{version}

%description -n %{name}+windows-sys
This metapackage enables feature "windows-sys" for the Rust io-lifetimes crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
