# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name shellexpand
%global full_version 3.1.2
%global pkgname shellexpand-3

Name:           rust-shellexpand-3
Version:        3.1.2
Release:        %autorelease
Summary:        Rust crate "shellexpand"
License:        MIT OR Apache-2.0
URL:            https://gitlab.com/ijackson/rust-shellexpand
#!RemoteAsset:  sha256:32824fab5e16e6c4d86dc1ba84489390419a39f97699852b66480bb87d297ed8
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

Patch0:         0001-fix-range-dependencies.patch

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/base-0) = %{version}

%description
Source code for takopackized Rust crate "shellexpand"

%package     -n %{name}+bstr
Summary:        Shell-like expansions in strings - feature "bstr"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bstr-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/bstr) = %{version}

%description -n %{name}+bstr
This metapackage enables feature "bstr" for the Rust shellexpand crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Shell-like expansions in strings - feature "default" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/base-0) = %{version}
Requires:       crate(%{pkgname}/tilde) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/full-msrv-1-31) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust shellexpand crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "full-msrv-1-31" feature.

%package     -n %{name}+dirs
Summary:        Shell-like expansions in strings - feature "dirs" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(dirs-6/default) >= 6.0.0
Provides:       crate(%{pkgname}/dirs) = %{version}
Provides:       crate(%{pkgname}/tilde) = %{version}

%description -n %{name}+dirs
This metapackage enables feature "dirs" for the Rust shellexpand crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "tilde" feature.

%package     -n %{name}+full-msrv-1-51
Summary:        Shell-like expansions in strings - feature "full-msrv-1-51" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/full-msrv-1-31) = %{version}
Requires:       crate(%{pkgname}/path) = %{version}
Provides:       crate(%{pkgname}/full) = %{version}
Provides:       crate(%{pkgname}/full-msrv-1-51) = %{version}

%description -n %{name}+full-msrv-1-51
This metapackage enables feature "full-msrv-1-51" for the Rust shellexpand crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "full" feature.

%package     -n %{name}+os-str-bytes
Summary:        Shell-like expansions in strings - feature "os_str_bytes"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(os-str-bytes-6/default) >= 6.0.0
Provides:       crate(%{pkgname}/os-str-bytes) = %{version}

%description -n %{name}+os-str-bytes
This metapackage enables feature "os_str_bytes" for the Rust shellexpand crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+path
Summary:        Shell-like expansions in strings - feature "path"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bstr) = %{version}
Requires:       crate(%{pkgname}/os-str-bytes) = %{version}
Provides:       crate(%{pkgname}/path) = %{version}

%description -n %{name}+path
This metapackage enables feature "path" for the Rust shellexpand crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
