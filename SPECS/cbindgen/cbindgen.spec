# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cbindgen
%global full_version 0.29.2

Name:           cbindgen
Version:        0.29.2
Release:        %autorelease
Summary:        Rust crate "cbindgen"
License:        MPL-2.0
URL:            https://github.com/mozilla/cbindgen
#!RemoteAsset:  sha256:befbfd072a8e81c02f8c507aefce431fe5e7d051f83d48a23ffc9b9fe5a11799
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildSystem:    rust

BuildOption(check):  -- --skip test_body

BuildRequires:  rust-rpm-macros
BuildRequires:  rust
BuildRequires:  cargo
BuildRequires:  python3dist(cython)
BuildRequires:  crate(clap-4/default) >= 4.3.0
BuildRequires:  crate(heck-0.5/default) >= 0.5.0
BuildRequires:  crate(indexmap-2/default) >= 2.1.0
BuildRequires:  crate(log-0.4/default) >= 0.4.0
BuildRequires:  crate(proc-macro2-1) >= 1.0.60
BuildRequires:  crate(proc-macro2-1/default) >= 1.0.60
BuildRequires:  crate(quote-1/default) >= 1.0.0
BuildRequires:  crate(serde-1/derive) >= 1.0.103
BuildRequires:  crate(serde-1/std) >= 1.0.103
BuildRequires:  crate(serde-json-1) >= 1.0.0
BuildRequires:  crate(serde-json-1/default) >= 1.0.0
BuildRequires:  crate(syn-2/clone-impls) >= 2.0.85
BuildRequires:  crate(syn-2/extra-traits) >= 2.0.85
BuildRequires:  crate(syn-2/fold) >= 2.0.85
BuildRequires:  crate(syn-2/full) >= 2.0.85
BuildRequires:  crate(syn-2/parsing) >= 2.0.85
BuildRequires:  crate(syn-2/printing) >= 2.0.85
BuildRequires:  crate(tempfile-3/default) >= 3.0.0
BuildRequires:  crate(toml-0.9/parse) >= 0.9.0
BuildRequires:  crate(toml-0.9/serde) >= 0.9.0
BuildRequires:  crate(toml-0.9/std) >= 0.9.0
BuildRequires:  crate(pretty-assertions-1/default) >= 1.4.0
BuildRequires:  crate(serial-test-2/default) >= 2.0.0
BuildRequires:  crate(getrandom-0.4/default) >= 0.4.0

%description
binary file of Rust crate "cbindgen".

%install
install -D -m 0755 target/release/cbindgen %{buildroot}%{_bindir}/cbindgen

%files
%{_bindir}/cbindgen

%changelog
%autochangelog
