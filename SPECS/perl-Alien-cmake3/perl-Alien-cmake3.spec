# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Alien-cmake3
Version:        0.10
Release:        %autorelease
Summary:        Find or download or build cmake 3
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Alien-cmake3
#!RemoteAsset:  sha256:c87a09d8687b5c5057b825c56329513d8b1b7741b1ec4fca346465ee0219485f
Source0:        https://www.cpan.org/authors/id/P/PL/PLICEASE/Alien-cmake3-%{version}.tar.gz
BuildSystem:    perlmaker

# the source code only allows cmake3.
Patch2000:      2000-enable-cmake4.patch

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  cmake
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.8.1
BuildRequires:  perl(Alien::Base) >= 0.92
BuildRequires:  perl(Alien::Build) >= 0.32
BuildRequires:  perl(Alien::Build::MM) >= 0.32
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test2::V0) >= 0.000121
BuildRequires:  perl(Test::Alien) >= 0.92
BuildRequires:  perl(File::chdir)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(Mojo::DOM58)
BuildRequires:  perl(Sort::Versions)
BuildRequires:  perl(IO::Socket::SSL)
BuildRequires:  perl(Mozilla::CA)

Requires:       perl(Alien::Base) >= 0.92

%description
This Alien distribution provides an external dependency on the build tool
cmake version 3.x.x. cmake is a popular alternative to autoconf.

%build -p
export ALIEN_INSTALL_TYPE=system

%files -f %{name}.files
%doc alienfile author.yml Changes perlcriticrc README

%changelog
%autochangelog
