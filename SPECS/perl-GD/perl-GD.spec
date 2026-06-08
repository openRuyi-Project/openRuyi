# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-GD
Version:        2.85
Release:        %autorelease
Summary:        GD Perl module
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/GD
#!RemoteAsset:  sha256:d897560cf138b04987dc016f662d9240f86c8241dc9c894aec0c8476013b1dbc
Source0:        https://www.cpan.org/authors/id/R/RU/RURBAN/GD-%{version}.tar.gz
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor OPTIMIZE="%{optflags}"

BuildRequires:  make
BuildRequires:  pkgconfig(gdlib)
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Math::Trig)
BuildRequires:  perl(Test::Fork) >= 0.02
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::NoWarnings) >= 1.00
BuildRequires:  perl(File::Which)
BuildRequires:  perl(ExtUtils::PkgConfig)

%description
GD.pm is a Perl interface to Thomas Boutell's gd graphics library (version
2.01 or higher; see below). GD allows you to create color drawings using a
large number of graphics primitives, and emit the drawings as PNG files.

%files -f %{name}.files
%doc ChangeLog const-c.inc const-xs.inc README README.QUICKDRAW testcpan.sh testlibs.sh

%changelog
%autochangelog
