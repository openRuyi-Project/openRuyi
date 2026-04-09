# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Crypt-URandom
Version:        0.54
Release:        %autorelease
Summary:        Provide non blocking randomness
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Crypt-URandom
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/D/DD/DDICK/Crypt-URandom-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.0
BuildRequires:  perl(Carp) >= 1.26
BuildRequires:  perl(constant)
BuildRequires:  perl(Encode)
BuildRequires:  perl(English)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod) >= 1.14

Requires:       perl(Carp) >= 1.26

%description
This Module is intended to provide an interface to the strongest available
source of non-blocking randomness on the current platform. Platforms
currently supported are anything supporting getrandom(2), /dev/urandom and
versions of Windows greater than or equal to Windows 2000.

%prep
%setup -q -n Crypt-URandom-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%{make_build}

%install
%perl_make_install
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes check_random.inc README README.md SECURITY.md

%changelog
%autochangelog
