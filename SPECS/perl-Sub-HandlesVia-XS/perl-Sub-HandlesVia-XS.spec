# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Sub-HandlesVia-XS
Version:        0.003004
Release:        %autorelease
Summary:        XS parts for Sub::HandlesVia; no user-serviceable parts inside
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Sub-HandlesVia-XS
#!RemoteAsset:  sha256:f854d358ea0d872cc09fa9c2b368fa070dc7898289b58fc9f1553abdbf85fb08
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/Sub-HandlesVia-XS-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test2::Plugin::BailOnFail)
BuildRequires:  perl(Test2::Require::AuthorTesting)
BuildRequires:  perl(Test2::Require::Module)
BuildRequires:  perl(Test2::Tools::Spec)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(Types::Common) >= 2.010001
Requires:       perl(Types::Common) >= 2.010001

%description
Use Sub::HandlesVia. That module will make use of Sub::HandlesVia::XS
when it can.

%prep
%setup -q -n Sub-HandlesVia-XS-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;

%files -f %{name}.files
%doc CREDITS Changes README doap.ttl
%license COPYRIGHT LICENSE
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Sub*

%changelog
%autochangelog
