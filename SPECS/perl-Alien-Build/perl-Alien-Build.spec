# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Alien-Build
Version:        2.84
Release:        %autorelease
Summary:        Build external dependencies for use in CPAN
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Alien-Build
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/P/PL/PLICEASE/Alien-Build-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl >= 5.8.4
BuildRequires:  perl(Capture::Tiny) >= 0.17
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.64
BuildRequires:  perl(ExtUtils::ParseXS) >= 3.30
BuildRequires:  perl(FFI::CheckLib) >= 0.11
BuildRequires:  perl(File::chdir)
BuildRequires:  perl(File::Which) >= 1.10
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(List::Util) >= 1.33
BuildRequires:  perl(parent)
BuildRequires:  perl(Path::Tiny) >= 0.077
BuildRequires:  perl(Test2::API) >= 1.302096
BuildRequires:  perl(Test2::V0) >= 0.000121
BuildRequires:  perl(Text::ParseWords) >= 3.26

Requires:       perl(Capture::Tiny) >= 0.17
Requires:       perl(ExtUtils::MakeMaker) >= 6.64
Requires:       perl(ExtUtils::ParseXS) >= 3.30
Requires:       perl(FFI::CheckLib) >= 0.11
Requires:       perl(File::Which) >= 1.10
Requires:       perl(List::Util) >= 1.33
Requires:       perl(Path::Tiny) >= 0.077
Requires:       perl(Test2::API) >= 1.302096
Requires:       perl(Text::ParseWords) >= 3.26

%description
This module provides tools for building external (non-CPAN) dependencies
for CPAN. It is mainly designed to be used at install time of a CPAN
client, and work closely with Alien::Base which is used at runtime.

%prep
%setup -q -n Alien-Build-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%{make_build}

%install
%perl_make_install
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc author.yml Changes Changes.Alien-Base Changes.Alien-Base-Wrapper Changes.Alien-Build-Decode-Mojo Changes.Test-Alien perlcriticrc README spellcheck.ini SUPPORT weaver.ini

%changelog
%autochangelog
