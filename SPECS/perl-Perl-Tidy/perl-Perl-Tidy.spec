# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Perl-Tidy
Version:        20260204
Release:        %autorelease
Summary:        Parses and beautifies perl source
License:        GPL-2.0-only
URL:            https://metacpan.org/dist/Perl-Tidy
#!RemoteAsset:  sha256:56a1fc2f1f813e49026a0f284b9209a6b2824620993e7598c85b01c444ff0f64
Source0:        https://www.cpan.org/authors/id/S/SH/SHANCOCK/Perl-Tidy-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.8.1
BuildRequires:  perl(ExtUtils::MakeMaker)

%description
This module makes the functionality of the perltidy utility available to
perl scripts. Any or all of the input parameters may be omitted, in which
case the @ARGV array will be used to provide input parameters as described
in the perltidy(1) man page.

%files -f %{name}.files
%doc BUGS.md CHANGES.md INSTALL.md pm2pl README.md SECURITY.md

%changelog
%autochangelog
