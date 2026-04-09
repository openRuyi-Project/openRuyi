# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Authen-SASL
Version:        2.1900
Release:        %autorelease
Summary:        SASL Authentication framework
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Authen-SASL
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/E/EH/EHUELS/Authen-SASL-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.14.0
BuildRequires:  perl(Crypt::URandom)
BuildRequires:  perl(Digest::HMAC_MD5)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(GSSAPI)
BuildRequires:  perl(Pod::Coverage::TrustPod)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)

%description
SASL is a generic mechanism for authentication used by several network
protocols. Authen::SASL provides an implementation framework that all
protocols should be able to share.

%prep
%setup -q -n Authen-SASL-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc api.txt Changes eg README

%changelog
%autochangelog
