# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-JSON-MaybeXS
Version:        1.004008
Release:        %autorelease
Summary:        Use Cpanel::JSON::XS with a fallback to JSON::XS and JSON::PP
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/JSON-MaybeXS
#!RemoteAsset:  sha256:cd3937afa78831f80a2ad5abab6c51b9e82fca4c31e5856ea208d598db5dc867
Source0:        https://cpan.metacpan.org/modules/by-module/JSON/JSON-MaybeXS-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(lib)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(Config)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(ExtUtils::Mksymlists)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(if)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

%description
This module first checks to see if either Cpanel::JSON::XS or JSON::XS
is already loaded, in which case it uses that module. Otherwise it tries
to load Cpanel::JSON::XS, then JSON::XS, then JSON::PP in order, and
either uses the first module it finds or throws an error.

It then exports the "encode_json" and "decode_json" functions from the
loaded module, along with a "JSON" constant that returns the class name
for calling "new" on.

If you're writing fresh code rather than replacing JSON.pm usage, you
might want to pass options as constructor args rather than calling
mutators, so we provide our own "new" method that supports that.

%prep
%setup -q -n JSON-MaybeXS-%{version}

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
