# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-MailTools
Version:        2.22
Release:        %autorelease
Summary:        Bundle of ancient email modules
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/MailTools
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/M/MA/MARKOV/MailTools-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(Date::Format)
BuildRequires:  perl(Date::Parse)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(Net::Domain) >= 1.05
BuildRequires:  perl(Net::SMTP) >= 1.28
BuildRequires:  perl(Test::More)

Requires:       perl(Net::Domain) >= 1.05
Requires:       perl(Net::SMTP) >= 1.28

%description
MailTools is a bundle: an ancient form of combining packages into one
distribution. Gladly, it can be distributed as if it is a normal
distribution as well.

%prep
%setup -q -n MailTools-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc ChangeLog MailTools.ppd README README.demos README.md

%changelog
%autochangelog
