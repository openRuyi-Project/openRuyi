# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Net-Daemon
Version:        0.52
Release:        %autorelease
Summary:        Perl extension for portable daemons
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Net-Daemon
#!RemoteAsset:  sha256:9635b16bdd4a0cf53d7a78479bfcd39b410c8bffd14d3eb37beca55130e36dce
Source0:        https://www.cpan.org/authors/id/T/TO/TODDR/Net-Daemon-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    perlmaker

BuildOption(build):  INSTALLDIRS=vendor

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.6.0
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Sys::Syslog) >= 0.29
BuildRequires:  perl(Test::More)

Requires:       perl(Sys::Syslog) >= 0.29

%description
Net::Daemon is an abstract base class for implementing portable server
applications in a very simple way. The module is designed for Perl 5.006
and ithreads, but can work with fork() as well.

%files -f %{name}.files
%doc AI_POLICY.md ChangeLog README.md

%changelog
%autochangelog
