# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Net-SMTP-SSL
Version:        1.04
Release:        %autorelease
Summary:        SSL support for Net::SMTP
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Net-SMTP-SSL
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/R/RJ/RJBS/Net-SMTP-SSL-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::Socket::SSL)
BuildRequires:  perl(Net::SMTP)
BuildRequires:  perl(Test::More) >= 0.47

Requires:       perl(Test::More) >= 0.47

%description
Implements the same API as Net::SMTP, but uses IO::Socket::SSL for its
network operations. Due to the nature of Net::SMTP's new method, it is not
overridden to make use of a default port for the SMTPS service. Perhaps
future versions will be smart like that. Port 465 is usually what you want,
and it's not a pain to specify that.

%prep
%setup -q -n Net-SMTP-SSL-%{version}

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
