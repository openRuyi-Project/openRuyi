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
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/M/MA/MATTN/Devel-CheckLib-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
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

%prep
%setup -q -n Devel-CheckLib-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%{make_build}

%install
%perl_make_install
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc CHANGES README TODO VMS-notes

%changelog
%autochangelog
