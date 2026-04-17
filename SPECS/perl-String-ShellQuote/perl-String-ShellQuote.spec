# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-String-ShellQuote
Version:        1.04
Release:        %autorelease
Summary:        Quote strings for passing through the shell
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/String-ShellQuote
#!RemoteAsset:  sha256:e606365038ce20d646d255c805effdd32f86475f18d43ca75455b00e4d86dd35
Source0:        https://cpan.metacpan.org/authors/id/R/RO/ROSCH/String-ShellQuote-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)

%description
This module contains some functions which are useful for quoting strings
which are going to pass through the shell or a shell-like object.

%prep
%setup -q -n String-ShellQuote-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README shell-quote test.t
%license

%changelog
%autochangelog
