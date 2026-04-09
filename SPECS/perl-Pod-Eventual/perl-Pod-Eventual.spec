# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Pod-Eventual
Version:        0.094003
Release:        %autorelease
Summary:        Read a POD document as a series of trivial events
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Pod-Eventual
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/R/RJ/RJBS/Pod-Eventual-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.12.0
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Mixin::Linewise::Readers) >= 0.102
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(warnings)

Requires:       perl(Mixin::Linewise::Readers) >= 0.102

%description
POD is a pretty simple format to write, but it can be a big pain to deal
with reading it and doing anything useful with it. Most existing POD
parsers care about semantics, like whether a =item occurred after an
=over but before a back, figuring out how to link a L<>, and other things
like that.

%prep
%setup -q -n Pod-Eventual-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README

%changelog
%autochangelog
