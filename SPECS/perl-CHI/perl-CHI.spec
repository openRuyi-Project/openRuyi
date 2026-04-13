# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-CHI
Version:        0.61
Release:        %autorelease
Summary:        Unified cache handling interface
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/CHI
#!RemoteAsset:  sha256:583545c9e5312bb4193ab16de9f55ff8f4b4a7ded128cee8dd2cb021d4678b5b
Source0:        https://cpan.metacpan.org/authors/id/A/AS/ASB/CHI-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(Cache::FileCache)
BuildRequires:  perl(Carp::Assert) >= 0.20
BuildRequires:  perl(Class::Load)
BuildRequires:  perl(Date::Parse)
BuildRequires:  perl(Data::UUID)
BuildRequires:  perl(Digest::JHash)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec) >= 0.80
BuildRequires:  perl(Hash::MoreUtils)
BuildRequires:  perl(JSON::MaybeXS) >= 1.003003
BuildRequires:  perl(List::MoreUtils) >= 0.13
BuildRequires:  perl(Log::Any) >= 0.08
BuildRequires:  perl(Module::Mask)
BuildRequires:  perl(Moo) >= 1.003
BuildRequires:  perl(MooX::Types::MooseLike) >= 0.23
BuildRequires:  perl(MooX::Types::MooseLike::Base)
BuildRequires:  perl(MooX::Types::MooseLike::Numeric)
BuildRequires:  perl(Storable)
BuildRequires:  perl(String::RewritePrefix)
BuildRequires:  perl(Task::Weaken)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::Class)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Warn)
BuildRequires:  perl(Time::Duration) >= 1.06
BuildRequires:  perl(Time::Duration::Parse) >= 0.03
BuildRequires:  perl(Time::HiRes) >= 1.30
BuildRequires:  perl(Try::Tiny) >= 0.05
Requires:       perl(Carp::Assert) >= 0.20
Requires:       perl(File::Spec) >= 0.80
Requires:       perl(JSON::MaybeXS) >= 1.003003
Requires:       perl(List::MoreUtils) >= 0.13
Requires:       perl(Log::Any) >= 0.08
Requires:       perl(Moo) >= 1.003
Requires:       perl(MooX::Types::MooseLike) >= 0.23
Requires:       perl(Time::Duration) >= 1.06
Requires:       perl(Time::Duration::Parse) >= 0.03
Requires:       perl(Time::HiRes) >= 1.30
Requires:       perl(Try::Tiny) >= 0.05
Requires:       perl(Data::UUID)
Requires:       perl(String::RewritePrefix)

%description
CHI provides a unified caching API, designed to assist a developer in
persisting data for a specified period of time.

%prep
%setup -q -n CHI-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files -f %{name}.files
%doc Changes
%license LICENSE

%changelog
%autochangelog
