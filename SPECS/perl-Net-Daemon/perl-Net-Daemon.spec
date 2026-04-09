# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Net-Daemon
Version:        0.49
Release:        %autorelease
Summary:        Perl extension for portable daemons
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Net-Daemon
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/T/TO/TODDR/Net-Daemon-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Sys::Syslog) >= 0.29

Requires:       perl(Sys::Syslog) >= 0.29

%description
Net::Daemon is an abstract base class for implementing portable server
applications in a very simple way. The module is designed for Perl 5.005
and threads, but can work with fork() and Perl 5.004.

%prep
%setup -q -n Net-Daemon-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc ChangeLog README

%changelog
%autochangelog
