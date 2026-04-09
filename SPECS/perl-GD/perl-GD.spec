# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-GD
Version:        2.83
Release:        %autorelease
Summary:        GD Perl module
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/GD
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/R/RU/RURBAN/GD-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  pkgconfig(gdlib)
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::Constant) >= 0.23
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(ExtUtils::PkgConfig)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(Carp)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(Math::Trig)
BuildRequires:  perl(strict)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(vars)
BuildRequires:  perl(Test::Fork) >= 0.02
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::NoWarnings) >= 1.00

%description
GD.pm is a Perl interface to Thomas Boutell's gd graphics library (version
2.01 or higher; see below). GD allows you to create color drawings using a
large number of graphics primitives, and emit the drawings as PNG files.

%prep
%setup -q -n GD-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%{make_build}

%install
%perl_make_install
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc ChangeLog const-c.inc const-xs.inc README README.QUICKDRAW testcpan.sh testlibs.sh

%changelog
%autochangelog
