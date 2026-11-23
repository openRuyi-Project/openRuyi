# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name xterm-color
%global full_version 1.0.0
%global pkgname xterm-color-1

Name:           rust-xterm-color-1
Version:        1.0.0
Release:        %autorelease
Summary:        Rust crate "xterm-color"
License:        MIT OR Apache-2.0
URL:            https://github.com/bash/terminal-colorsaurus
#!RemoteAsset:  sha256:1290e4814480cacefbbb0e57c9f1a21667d03d0c4fe4d0753ee4a1429b7d26bf
Source:         https://static.crates.io/crates/xterm-color/1.0.0/download#/rust-xterm-color-1-1.0.0.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "xterm-color"

%package     -n %{name}+default
Summary:        Parses the subset of X11 Color Strings emitted by terminals in response to OSC color queries - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust xterm-color crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
