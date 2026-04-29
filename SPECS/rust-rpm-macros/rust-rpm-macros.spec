# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           rust-rpm-macros
Version:        0.4
Release:        %autorelease
Summary:        Rust macros for openRuyi packaging
License:        MIT
URL:            https://github.com/openRuyi-Project/rust-rpm-macros
#!RemoteAsset:  sha256:b09e1db2b1fd8dea5567832c1090ef163bfdf5d8a1f1c6fbce0c71c01464aec2
Source0:        https://github.com/openRuyi-Project/rust-rpm-macros/archive/refs/tags/v%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    autotools

%description
This package provides RPM macros for packaging Rust software in openRuyi.

%conf
# No configure

# No build needed
%build

# No check needed
%check

%files
%license LICENSE
%{_rpmmacrodir}/macros.buildsystem.rustcrates
%{_rpmmacrodir}/macros.buildsystem.rust
%{_rpmmacrodir}/macros.rust
%{_rpmconfigdir}/rust-rpm-macros/rustcrates-gen-feature-specparts.sh
%{_rpmconfigdir}/rust-rpm-macros/cargo_buildrequires.sh

%changelog
%autochangelog
