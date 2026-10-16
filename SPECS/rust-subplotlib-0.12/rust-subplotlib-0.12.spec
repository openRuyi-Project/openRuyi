# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name subplotlib
%global full_version 0.12.0
%global pkgname subplotlib-0.12

Name:           rust-subplotlib-0.12
Version:        0.12.0
Release:        %autorelease
Summary:        Rust crate "subplotlib"
License:        MIT-0
URL:            https://subplot.tech/
#!RemoteAsset:  sha256:6ddf898c1d4ef62f77028b546f7baf9c1e661c927587249da0b0fa5ec5906422
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(base64-0.22/default) >= 0.22.1
Requires:       crate(culpa-1/default) >= 1.0.1
Requires:       crate(filetime-0.2/default) >= 0.2.9
Requires:       crate(fs2-0.4/default) >= 0.4.0
Requires:       crate(lazy-static-1/default) >= 1.0.0
Requires:       crate(regex-1/default) >= 1.4.0
Requires:       crate(remove-dir-all-1/default) >= 1.0.0
Requires:       crate(shell-words-1/default) >= 1.0.0
Requires:       crate(state-0.6/default) >= 0.6.0
Requires:       crate(subplotlib-derive-0.12/default) >= 0.12.0
Requires:       crate(tempfile-3/default) >= 3.1.0
Requires:       crate(time-0.3/default) >= 0.3.0
Requires:       crate(time-0.3/macros) >= 0.3.0
Requires:       crate(time-0.3/parsing) >= 0.3.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Relies on `subplotlib-derive` for associated macros.
Source code for takopackized Rust crate "subplotlib"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
