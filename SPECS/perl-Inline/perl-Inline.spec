# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Inline
Version:        0.87
Release:        %autorelease
Summary:        Write Perl Subroutines in Other Programming Languages
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Inline
#!RemoteAsset:  sha256:105e4271ace1c1b5a264d771ff111d8b928b256002888222862c7be9686f39c5
Source0:        https://cpan.metacpan.org/authors/id/I/IN/INGY/Inline-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec) >= 0.8
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Warn) >= 0.23
BuildRequires:  perl(version) >= 0.82
Requires:       perl(File::Spec) >= 0.8
Requires:       perl(version) >= 0.82

%description
The Inline module allows you to put source code from other programming
languages directly "inline" in a Perl script or module. The code is
automatically compiled as needed, and then loaded for immediate access
from Perl.

%prep
%setup -q -n Inline-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc CONTRIBUTING Changes README
%license LICENSE

%changelog
%autochangelog
