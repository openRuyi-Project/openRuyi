# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Pegex
Version:        0.75
Release:        %autorelease
Summary:        Acmeist PEG Parser Framework
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Pegex
#!RemoteAsset:  sha256:4dc8d335de80b25247cdb3f946f0d10d9ba0b3c34b0ed7d00316fd068fd05edc
Source0:        https://cpan.metacpan.org/authors/id/I/IN/INGY/Pegex-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::ShareDir::Install)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Tie::IxHash)
BuildRequires:  perl(XXX) >= 0.35
BuildRequires:  perl(YAML::PP) >= 0.019
Requires:       perl(XXX) >= 0.35
Requires:       perl(YAML::PP) >= 0.019

%description
Pegex is an Acmeist parser framework. It allows you to easily create
parsers that will work equivalently in lots of programming languages! The
inspiration for Pegex comes from the parsing engine upon which the
postmodern programming language Perl 6 is based on. Pegex brings this
beauty to the other justmodern languages that have a normal regular
expression engine available.

%prep
%setup -q -n Pegex-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc CONTRIBUTING Changes README example share xt
%license LICENSE

%changelog
%autochangelog
