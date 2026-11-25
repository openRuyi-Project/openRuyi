# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name qbase
%global full_version 0.7.0
%global pkgname qbase-0.7

Name:           rust-qbase-0.7
Version:        0.7.0
Release:        %autorelease
Summary:        Rust crate "qbase"
License:        Apache-2.0
URL:            https://github.com/genmeta/dquic
#!RemoteAsset:  sha256:78f8b7a61a7395f50d7e445be878b2b1bfd0724659283c67a58d777230ec66e2
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2/default) >= 2.0.0
Requires:       crate(bytes-1/default) >= 1.0.0
Requires:       crate(derive-more-2/as-ref) >= 2.0.0
Requires:       crate(derive-more-2/default) >= 2.0.0
Requires:       crate(derive-more-2/deref) >= 2.0.0
Requires:       crate(derive-more-2/deref-mut) >= 2.0.0
Requires:       crate(derive-more-2/display) >= 2.0.0
Requires:       crate(derive-more-2/from) >= 2.0.0
Requires:       crate(derive-more-2/into) >= 2.0.0
Requires:       crate(derive-more-2/try-into) >= 2.0.0
Requires:       crate(enum-dispatch-0.3/default) >= 0.3.0
Requires:       crate(futures-0.3/default) >= 0.3.0
Requires:       crate(getset-0.1/default) >= 0.1.0
Requires:       crate(nom-8/default) >= 8.0.0
Requires:       crate(qmacro-0.6/default) >= 0.6.0
Requires:       crate(qtls-0.1/default) >= 0.1.0
Requires:       crate(rand-0.10/default) >= 0.10.0
Requires:       crate(rustls-0.23/std) >= 0.23.0
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Requires:       crate(smallvec-1/const-generics) >= 1.0.0
Requires:       crate(smallvec-1/const-new) >= 1.0.0
Requires:       crate(smallvec-1/default) >= 1.0.0
Requires:       crate(smallvec-1/union) >= 1.0.0
Requires:       crate(thiserror-2/default) >= 2.0.20
Requires:       crate(tokio-1/default) >= 1.0.0
Requires:       crate(tokio-1/rt) >= 1.0.0
Requires:       crate(tokio-1/sync) >= 1.0.0
Requires:       crate(tokio-1/time) >= 1.0.0
Requires:       crate(tracing-0.1/default) >= 0.1.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "qbase"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
