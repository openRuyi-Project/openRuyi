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
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros
BuildRequires:  rust
BuildRequires:  crate(heck-0.5/default) >= 0.5.0
BuildRequires:  crate(indexmap-2.0/default) >= 2.1.0
BuildRequires:  crate(log-0.4/default) >= 0.4.0
BuildRequires:  crate(proc-macro2-1.0/default) >= 1.0.60
BuildRequires:  crate(quote-1.0/default) >= 1.0.0
BuildRequires:  crate(serde-1.0/derive) >= 1.0.103
BuildRequires:  crate(serde-1.0/std) >= 1.0.103
BuildRequires:  crate(serde-json-1.0/default) >= 1.0.0
BuildRequires:  crate(syn-2.0/clone-impls) >= 2.0.85
BuildRequires:  crate(syn-2.0/extra-traits) >= 2.0.85
BuildRequires:  crate(syn-2.0/fold) >= 2.0.85
BuildRequires:  crate(syn-2.0/full) >= 2.0.85
BuildRequires:  crate(syn-2.0/parsing) >= 2.0.85
BuildRequires:  crate(syn-2.0/printing) >= 2.0.85
BuildRequires:  crate(tempfile-3.0/default) >= 3.0.0
BuildRequires:  crate(toml-0.9/parse) >= 0.9.0
BuildRequires:  crate(toml-0.9/serde) >= 0.9.0
BuildRequires:  crate(toml-0.9/std) >= 0.9.0
BuildRequires:  crate(pretty-assertions-1.0) >= 1.4.0
BuildRequires:  crate(serial-test-2.0) >= 2.0.0
BuildRequires:  crate(clap-4.0/default) >= 4.3

%description
binary file of Rust crate "cbindgen".

%prep -a
mkdir -p ~/.cargo
cat > ~/.cargo/config.toml <<EOF
[source.crates-io]
replace-with = "system-registry"

[source.system-registry]
directory = "/usr/share/cargo/registry"
EOF

rm -rf Cargo.lock

%build
cargo build --release

%install -a
install -Dm0755 target/release/cbindgen %{buildroot}%{_bindir}/cbindgen

%files
%{_bindir}/cbindgen
%exclude %{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
