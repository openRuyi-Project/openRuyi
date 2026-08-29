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
#!RemoteAsset:  sha256:3bf68bb212298fa699a52749dddff35583a74f36a92ca89c843b854f29d87c77
Source0:        https://www.cpan.org/authors/id/M/MA/MARKOV/MailTools-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
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

%files -f %{name}.files
%doc ChangeLog MailTools.ppd README README.demos README.md

%changelog
%autochangelog
