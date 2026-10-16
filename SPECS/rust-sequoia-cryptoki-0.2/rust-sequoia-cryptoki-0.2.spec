# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name sequoia-cryptoki
%global full_version 0.2.0
%global pkgname sequoia-cryptoki-0.2

Name:           rust-sequoia-cryptoki-0.2
Version:        0.2.0
Release:        %autorelease
Summary:        Rust crate "sequoia-cryptoki"
License:        LGPL-2.0-or-later AND CC-BY-4.0
URL:            https://gitlab.com/sequoia-pgp/sequoia-cryptoki
#!RemoteAsset:  sha256:777bafa03ef7f6f41a7eb3f9f3b87e0de26c468775edd60382aa1cb899189860
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(aho-corasick-1/default) >= 1.0.0
Requires:       crate(anyhow-1/default) >= 1.0.18
Requires:       crate(chrono-0.4/default) >= 0.4.38
Requires:       crate(cryptoki-0.12/default) >= 0.12.0
Requires:       crate(dirs-5/default) >= 5.0.0
Requires:       crate(log-0.4/default) >= 0.4.0
Requires:       crate(regex-1/default) >= 1.0.0
Requires:       crate(sequoia-directories-0.1/default) >= 0.1.0
Requires:       crate(sequoia-openpgp-2) >= 2.4.0
Requires:       crate(tempfile-3/default) >= 3.1.0
Requires:       crate(thiserror-1/default) >= 1.0.0
Requires:       crate(toml-edit-0.22/display) >= 0.22.0
Requires:       crate(toml-edit-0.22/parse) >= 0.22.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "sequoia-cryptoki"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
