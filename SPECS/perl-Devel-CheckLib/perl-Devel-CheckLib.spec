# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Devel-CheckLib
Version:        1.16
Release:        %autorelease
Summary:        Check that a library is available
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Devel-CheckLib
#!RemoteAsset:  sha256:869d38c258e646dcef676609f0dd7ca90f085f56cf6fd7001b019a5d5b831fca
Source0:        https://www.cpan.org/authors/id/M/MA/MATTN/Devel-CheckLib-%{version}.tar.gz
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor OPTIMIZE="%{optflags}"

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.4.0
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp) >= 0.16
BuildRequires:  perl(Mock::Config) >= 0.02
BuildRequires:  perl(Test::More) >= 0.88

Requires:       perl(File::Temp) >= 0.16

%description
Devel::CheckLib is a perl module that checks whether a particular C library
and its headers are available.

%files -f %{name}.files
%doc CHANGES README TODO VMS-notes

%changelog
%autochangelog
