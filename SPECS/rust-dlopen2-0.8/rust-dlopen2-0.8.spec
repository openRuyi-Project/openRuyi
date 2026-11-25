# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name dlopen2
%global full_version 0.8.2
%global pkgname dlopen2-0.8

Name:           rust-dlopen2-0.8
Version:        0.8.2
Release:        %autorelease
Summary:        Rust crate "dlopen2"
License:        MIT
URL:            https://github.com/OpenByteDev/dlopen2
#!RemoteAsset:  sha256:5e2c5bd4158e66d1e215c49b837e11d62f3267b30c92f1d171c4d3105e3dc4d4
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.0
Requires:       crate(once-cell-1/default) >= 1.19.0
Requires:       crate(winapi-0.3/basetsd) >= 0.3.0
Requires:       crate(winapi-0.3/dbghelp) >= 0.3.0
Requires:       crate(winapi-0.3/default) >= 0.3.0
Requires:       crate(winapi-0.3/errhandlingapi) >= 0.3.0
Requires:       crate(winapi-0.3/libloaderapi) >= 0.3.0
Requires:       crate(winapi-0.3/minwindef) >= 0.3.0
Requires:       crate(winapi-0.3/processthreadsapi) >= 0.3.0
Requires:       crate(winapi-0.3/winerror) >= 0.3.0
Requires:       crate(winapi-0.3/winnt) >= 0.3.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/doc-cfg) = %{version}
Provides:       crate(%{pkgname}/symbor) = %{version}
Provides:       crate(%{pkgname}/wrapper) = %{version}

%description
Source code for takopackized Rust crate "dlopen2"

%package     -n %{name}+default
Summary:        Opening and operating on dynamic link libraries (also known as shared objects or shared libraries) - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/derive) = %{version}
Requires:       crate(%{pkgname}/symbor) = %{version}
Requires:       crate(%{pkgname}/wrapper) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust dlopen2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dlopen2-derive
Summary:        Opening and operating on dynamic link libraries (also known as shared objects or shared libraries) - feature "dlopen2_derive" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(dlopen2-derive-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/derive) = %{version}
Provides:       crate(%{pkgname}/dlopen2-derive) = %{version}

%description -n %{name}+dlopen2-derive
This metapackage enables feature "dlopen2_derive" for the Rust dlopen2 crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "derive" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
