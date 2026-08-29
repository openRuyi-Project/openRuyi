# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Module-Metadata
Version:        1.000039
Release:        %autorelease
Summary:        Gather package and POD information from perl module files
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Module-Metadata
#!RemoteAsset:  sha256:4c2bf998053d232df9e6262ea0ccad62abe87e448e62fdfe719949ea1a856c28
Source0:        https://www.cpan.org/authors/id/E/ET/ETHER/Module-Metadata-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.0
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(version) >= 0.87
BuildRequires:  perl(warnings)

Requires:       perl(version) >= 0.87

%description
This module provides a standard way to gather metadata about a .pm file
through (mostly) static analysis and (some) code execution. When
determining the version of a module, the $VERSION assignment is evaled, as
is traditional in the CPAN toolchain.

%files -f %{name}.files
%doc Changes CONTRIBUTING README weaver.ini

%changelog
%autochangelog
