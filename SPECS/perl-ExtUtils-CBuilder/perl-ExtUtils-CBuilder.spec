# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-ExtUtils-CBuilder
Version:        0.280236
Release:        %autorelease
Summary:        Compile and link C code for Perl modules
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/ExtUtils-CBuilder
#!RemoteAsset:  sha256:abc21827eb8a513171bf7fdecefce9945132cb76db945036518291f607b1491f
Source0:        https://www.cpan.org/authors/id/A/AM/AMBS/ExtUtils-CBuilder-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.30
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec) >= 3.13
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(Perl::OSType) >= 1
BuildRequires:  perl(Test::More) >= 0.47
BuildRequires:  perl(Text::ParseWords)

Requires:       perl(ExtUtils::MakeMaker) >= 6.30
Requires:       perl(File::Spec) >= 3.13
Requires:       perl(Perl::OSType) >= 1

%description
This module can build the C portions of Perl modules by invoking the
appropriate compilers and linkers in a cross-platform manner. It was
motivated by the Module::Build project, but may be useful for other
purposes as well. However, it is not intended as a general cross-platform
interface to all your C building needs. That would have been a much more
ambitious goal!

%files -f %{name}.files
%doc CONTRIBUTING Changes NOTAS-Alberto README README.mkdn README.patching README.release

%changelog
%autochangelog
