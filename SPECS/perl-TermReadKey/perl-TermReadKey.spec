# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-TermReadKey
Version:        2.38
Release:        %autorelease
Summary:        TermReadKey Perl module
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/TermReadKey
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/J/JS/JSTOWE/TermReadKey-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)

%description
Term::ReadKey is a compiled perl module dedicated to providing simple
control over terminal driver modes (cbreak, raw, cooked, etc.)
support for non-blocking reads, if the architecture allows, and some
generalized handy functions for working with terminals.

%prep
%setup -q -n TermReadKey-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%{make_build}

%install
%perl_make_install
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
