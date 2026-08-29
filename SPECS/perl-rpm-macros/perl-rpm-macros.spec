# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-rpm-macros
Version:        0.1
Release:        %autorelease
Summary:        perl macros for openRuyi packaging
License:        MIT
URL:            https://github.com/openRuyi-Project/perl-rpm-macros
#!RemoteAsset:  sha256:1d0224223cda79c343b2a3ab411013fdd8d59cd208a7441e09172a87baf0d8a2
Source0:        https://github.com/openRuyi-Project/perl-rpm-macros/archive/refs/tags/v%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    autotools

Requires:       perl-devel

%description
This package provides RPM macros for packaging perl software in openRuyi.

%conf
# No configure

# No build needed
%build

# No check needed
%check

%files
%license LICENSE
%{_rpmmacrodir}/macros.buildsystem.perlmaker
%{_rpmmacrodir}/macros.buildsystem.perlbuild

%changelog
%autochangelog
