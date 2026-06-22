# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name wasm-streams
%global full_version 0.5.0
%global pkgname wasm-streams-0.5

Name:           rust-wasm-streams-0.5
Version:        0.5.0
Release:        %autorelease
Summary:        Rust crate "wasm-streams"
License:        MIT OR Apache-2.0
URL:            https://github.com/MattiasBuelens/wasm-streams/
#!RemoteAsset:  sha256:9d1ec4f6517c9e11ae630e200b2b65d193279042e28edd4a2cda233e46670bbb
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(futures-util-0.3/default) >= 0.3.31
Requires:       crate(futures-util-0.3/io) >= 0.3.31
Requires:       crate(futures-util-0.3/sink) >= 0.3.31
Requires:       crate(js-sys-0.3/default) >= 0.3.85
Requires:       crate(wasm-bindgen-0.2/default) >= 0.2.108
Requires:       crate(wasm-bindgen-futures-0.4/default) >= 0.4.58
Requires:       crate(web-sys-0.3/abortsignal) >= 0.3.85
Requires:       crate(web-sys-0.3/default) >= 0.3.85
Requires:       crate(web-sys-0.3/queuingstrategy) >= 0.3.85
Requires:       crate(web-sys-0.3/readablebytestreamcontroller) >= 0.3.85
Requires:       crate(web-sys-0.3/readablestream) >= 0.3.85
Requires:       crate(web-sys-0.3/readablestreambyobreader) >= 0.3.85
Requires:       crate(web-sys-0.3/readablestreambyobrequest) >= 0.3.85
Requires:       crate(web-sys-0.3/readablestreamdefaultcontroller) >= 0.3.85
Requires:       crate(web-sys-0.3/readablestreamdefaultreader) >= 0.3.85
Requires:       crate(web-sys-0.3/readablestreamgetreaderoptions) >= 0.3.85
Requires:       crate(web-sys-0.3/readablestreamreadermode) >= 0.3.85
Requires:       crate(web-sys-0.3/readablestreamreadresult) >= 0.3.85
Requires:       crate(web-sys-0.3/readablestreamtype) >= 0.3.85
Requires:       crate(web-sys-0.3/readablewritablepair) >= 0.3.85
Requires:       crate(web-sys-0.3/streampipeoptions) >= 0.3.85
Requires:       crate(web-sys-0.3/transformer) >= 0.3.85
Requires:       crate(web-sys-0.3/transformstream) >= 0.3.85
Requires:       crate(web-sys-0.3/transformstreamdefaultcontroller) >= 0.3.85
Requires:       crate(web-sys-0.3/underlyingsink) >= 0.3.85
Requires:       crate(web-sys-0.3/underlyingsource) >= 0.3.85
Requires:       crate(web-sys-0.3/writablestream) >= 0.3.85
Requires:       crate(web-sys-0.3/writablestreamdefaultcontroller) >= 0.3.85
Requires:       crate(web-sys-0.3/writablestreamdefaultwriter) >= 0.3.85
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "wasm-streams"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
