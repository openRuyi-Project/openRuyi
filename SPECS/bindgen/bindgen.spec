# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name bindgen-cli
%global full_version 0.72.1

Name:           bindgen
Version:        0.72.1
Release:        %autorelease
Summary:        Automatically generates Rust FFI bindings to C and C++ libraries
License:        BSD-3-Clause
URL:            https://rust-lang.github.io/rust-bindgen/
VCS:            git:https://github.com/rust-lang/rust-bindgen
#!RemoteAsset:  sha256:8a408c0fcb20bf7bd4ceaf4bf990e223e3543a04b84d2394f3edeee29a0e87e2
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{crate_name}-%{version}.tar.gz
BuildSystem:    rust

BuildRequires:  rust-rpm-macros
BuildRequires:  rust
BuildRequires:  cargo
BuildRequires:  clang-devel
BuildRequires:  crate(bindgen-0.72/cli) >= 0.72.1
BuildRequires:  crate(bindgen-0.72/experimental) >= 0.72.1
BuildRequires:  crate(bindgen-0.72/logging) >= 0.72.1
BuildRequires:  crate(bindgen-0.72/prettyplease) >= 0.72.1
BuildRequires:  crate(bindgen-0.72/runtime) >= 0.72.1
BuildRequires:  crate(env-logger-0.10/default) >= 0.10.2
BuildRequires:  crate(log-0.4/default) >= 0.4.30
BuildRequires:  crate(proc-macro2-1/default) >= 1.0.106
BuildRequires:  crate(shlex-1/default) >= 1.3.0

Requires:       clang

%description
Automatically generates Rust FFI bindings to C and C++ libraries.
This package contains the bindgen command-line tool from the bindgen-cli crate.

%install
install -D -m 0755 target/release/bindgen %{buildroot}%{_bindir}/bindgen

# Shell completions
install -d %{buildroot}%{_datadir}/bash-completion/completions
install -d %{buildroot}%{_datadir}/fish/vendor_completions.d
install -d %{buildroot}%{_datadir}/zsh/site-functions

target/release/bindgen --generate-shell-completions bash \
  > %{buildroot}%{_datadir}/bash-completion/completions/bindgen

target/release/bindgen --generate-shell-completions fish \
  > %{buildroot}%{_datadir}/fish/vendor_completions.d/bindgen.fish

target/release/bindgen --generate-shell-completions zsh \
  > %{buildroot}%{_datadir}/zsh/site-functions/_bindgen

%files
%doc README.md
%license LICENSE
%{_bindir}/bindgen
%{_datadir}/bash-completion/completions/bindgen
%{_datadir}/fish/vendor_completions.d/bindgen.fish
%{_datadir}/zsh/site-functions/_bindgen

%changelog
%autochangelog
