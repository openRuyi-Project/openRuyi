# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global commit f5ce3e235f98cf1cd0123910439ce38c7294c165

Name:           cargo-buckal-bundles
Version:        0.20260803
Release:        %autorelease
Summary:        Buck2 rules and helper scripts for Cargo projects
License:        MIT
URL:            https://github.com/buck2hub/buckal-bundles
VCS:            git:https://github.com/buck2hub/buckal-bundles.git
#!RemoteAsset:  sha256:1629bc71f8637793c95dac640e00b86652cba6f1066d0d65506a4bb86c742fa2
Source:         %{url}/archive/%{commit}/buckal-bundles-%{commit}.tar.gz
# Update integration with the Buck2 2026-11-15 Rust prelude.
Patch2000:      2000-adapt-rust-buildscript-rules.patch
BuildArch:      noarch
BuildRequires:  python3
Requires:       python3

%description
Buckal Bundles provides Starlark rules and helper scripts that let
cargo-buckal migrate Cargo projects to Buck2. The installed files can
be copied into a project and used as its local buckal cell.

%prep
%autosetup -p1 -n buckal-bundles-%{commit}

%build
# The bundle contains Starlark rules and Python sources.

%install
dest=%{buildroot}%{_datadir}/cargo-buckal/bundles
install -d "$dest"
cp -a *.bzl config tool "$dest/"

%check
python3 -m py_compile tool/*.py

%files
%license LICENSE
%doc README.md
%{_datadir}/cargo-buckal/

%changelog
%autochangelog
