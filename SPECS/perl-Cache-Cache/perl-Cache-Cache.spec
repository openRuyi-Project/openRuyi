# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Cache-Cache
Version:        1.08
Release:        %autorelease
Summary:        Cache interface
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Cache-Cache
#!RemoteAsset:  sha256:d2c7fd5dba5dd010b7d8923516890bb6ccf6b5f188ccb69f35cb0fd6c031d1e8
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Cache-Cache-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(Digest::SHA1) >= 2.02
BuildRequires:  perl(Error) >= 0.15
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec) >= 0.82
BuildRequires:  perl(IPC::ShareLite) >= 0.09
BuildRequires:  perl(Storable) >= 1.014
Requires:       perl(Digest::SHA1) >= 2.02
Requires:       perl(Error) >= 0.15
Requires:       perl(File::Spec) >= 0.82
Requires:       perl(IPC::ShareLite) >= 0.09
Requires:       perl(Storable) >= 1.014

%description
The Cache modules are designed to assist a developer in persisting data for
a specified period of time. Often these modules are used in web
applications to store data locally to save repeated and redundant expensive
calls to remote machines or databases. People have also been known to use
Cache::Cache for its straightforward interface in sharing data between runs
of an application or invocations of a CGI-style script or simply as an easy
to use abstraction of the filesystem or shared memory.

%prep
%setup -q -n Cache-Cache-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc CHANGES CREDITS DISCLAIMER README STYLE
%license COPYING

%changelog
%autochangelog
