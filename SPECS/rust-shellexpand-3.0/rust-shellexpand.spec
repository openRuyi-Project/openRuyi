# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name shellexpand
%global full_version 3.1.2
%global pkgname shellexpand-3.0

Name:           rust-shellexpand-3.0
Version:        3.1.2
Release:        %autorelease
Summary:        Rust crate "shellexpand"
License:        MIT OR Apache-2.0
URL:            https://gitlab.com/ijackson/rust-shellexpand
#!RemoteAsset:  sha256:32824fab5e16e6c4d86dc1ba84489390419a39f97699852b66480bb87d297ed8
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/base-0)

%description
Source code for takopackized Rust crate "shellexpand"

%package     -n %{name}+default
Summary:        Shell-like expansions in strings - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/base-0)
Requires:       crate(%{pkgname}/tilde)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust shellexpand crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+full
Summary:        Shell-like expansions in strings - feature "full"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/full-msrv-1-51)
Provides:       crate(%{pkgname}/full)

%description -n %{name}+full
This metapackage enables feature "full" for the Rust shellexpand crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+full-msrv-1-31
Summary:        Shell-like expansions in strings - feature "full-msrv-1-31"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/base-0)
Requires:       crate(%{pkgname}/tilde)
Provides:       crate(%{pkgname}/full-msrv-1-31)

%description -n %{name}+full-msrv-1-31
This metapackage enables feature "full-msrv-1-31" for the Rust shellexpand crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+full-msrv-1-51
Summary:        Shell-like expansions in strings - feature "full-msrv-1-51"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/full-msrv-1-31)
Requires:       crate(%{pkgname}/path)
Provides:       crate(%{pkgname}/full-msrv-1-51)

%description -n %{name}+full-msrv-1-51
This metapackage enables feature "full-msrv-1-51" for the Rust shellexpand crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+path
Summary:        Shell-like expansions in strings - feature "path"
Requires:       crate(%{pkgname})
Requires:       crate(bstr-1.0/default) >= 1.12.1
Requires:       crate(os-str-bytes-7.0/default) >= 7.1.1
Provides:       crate(%{pkgname}/path)

%description -n %{name}+path
This metapackage enables feature "path" for the Rust shellexpand crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tilde
Summary:        Shell-like expansions in strings - feature "tilde"
Requires:       crate(%{pkgname})
Requires:       crate(dirs-6.0/default) >= 6.0.0
Provides:       crate(%{pkgname}/tilde)

%description -n %{name}+tilde
This metapackage enables feature "tilde" for the Rust shellexpand crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
