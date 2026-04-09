# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-IO-Socket-SSL
Version:        2.095
Release:        %autorelease
Summary:        SSL sockets with IO::Socket interface
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/IO-Socket-SSL
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/S/SU/SULLR/IO-Socket-SSL-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Mozilla::CA)
BuildRequires:  perl(Net::SSLeay) >= 1.46
BuildRequires:  perl(Scalar::Util)

Requires:       perl(Net::SSLeay) >= 1.46

%description
IO::Socket::SSL makes using SSL/TLS much easier by wrapping the necessary
functionality into the familiar IO::Socket interface and providing secure
defaults whenever possible. This way, existing applications can be made SSL-
aware without much effort, at least if you do blocking I/O and don't use
select or poll.

%prep
%setup -q -n IO-Socket-SSL-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc BUGS Changes README

%changelog
%autochangelog
