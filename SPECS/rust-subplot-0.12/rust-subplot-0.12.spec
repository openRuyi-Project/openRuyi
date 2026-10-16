# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name subplot
%global full_version 0.12.0
%global pkgname subplot-0.12

Name:           rust-subplot-0.12
Version:        0.12.0
Release:        %autorelease
Summary:        Rust crate "subplot"
License:        MIT-0
URL:            https://subplot.tech/
#!RemoteAsset:  sha256:5eb998cc5b2599ac493bd0fd2972013c3f3c11ef37800f6d2d2f4067d78a0c01
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anyhow-1) >= 1.0.0
Requires:       crate(base64-0.22/default) >= 0.22.1
Requires:       crate(descape-2/default) >= 2.0.3
Requires:       crate(getopts-0.2/default) >= 0.2.21
Requires:       crate(html-escape-0.2/default) >= 0.2.13
Requires:       crate(lazy-static-1/default) >= 1.0.0
Requires:       crate(line-col-0.2/default) >= 0.2.1
Requires:       crate(marked-yaml-0.7/default) >= 0.7.0
Requires:       crate(marked-yaml-0.7/serde-path) >= 0.7.0
Requires:       crate(pikchr-0.1/default) >= 0.1.0
Requires:       crate(pulldown-cmark-0.12/default) >= 0.12.0
Requires:       crate(regex-1/default) >= 1.0.0
Requires:       crate(roadmap-0.7) >= 0.7.0
Requires:       crate(serde-1/default) >= 1.0.101
Requires:       crate(serde-1/derive) >= 1.0.101
Requires:       crate(serde-json-1/default) >= 1.0.0
Requires:       crate(slug-0.1/default) >= 0.1.1
Requires:       crate(tera-1/humansize) >= 1.18.0
Requires:       crate(tera-1/percent-encoding) >= 1.18.0
Requires:       crate(tera-1/rand) >= 1.18.0
Requires:       crate(tera-1/slug) >= 1.18.0
Requires:       crate(thiserror-2/default) >= 2.0.0
Requires:       crate(tracing-0.1/default) >= 0.1.41
Requires:       crate(walkdir-2) >= 2.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "subplot"

%package     -n %{name}+unstable-cli
Summary:        Tools for specifying, documenting, and implementing automated acceptance tests for systems and software - feature "unstable-cli"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(clap-4/default) >= 4.0.0
Requires:       crate(clap-4/derive) >= 4.0.0
Requires:       crate(clap-4/env) >= 4.0.0
Requires:       crate(clap-4/string) >= 4.0.0
Provides:       crate(%{pkgname}/unstable-cli) = %{version}

%description -n %{name}+unstable-cli
This metapackage enables feature "unstable-cli" for the Rust subplot crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
