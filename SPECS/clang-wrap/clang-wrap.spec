# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: YunQiang Su <yunqiang@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global git_ver git20260525.d26e9b7
%global git_commit d26e9b77baa81df3adf1b410e08135a30873606e

Name:           clang-wrap
Version:        0+%{git_ver}
Release:        %{autorelease}
License:        Mulan-2.0
Summary:        clang-wrap to collect LLVM IR
URL:            https://github.com/openRuyi-Project/clang-wrap
#!RemoteAsset:  sha256:f6eeb35daec88135c047fe1d9c3e1960d69dfebb1d0041a336805f338807e76d
Source0:        https://github.com/openRuyi-Project/clang-wrap/archive/%{git_commit}.tar.gz
Source1:        macros.clang-wrap
BuildSystem:    rust

BuildRequires:  cargo
BuildRequires:  rust
BuildRequires:  rust-rpm-macros
BuildRequires:  crate(pathdiff-0.2/default)

%description
%{summary}

This package contains wrap of clang, clang++, ar, cp, install, strip.
These wrappers work on normal object and the IR files at the same time.

%{load:%{SOURCE1}}

%install
install -p -m0644 -D %{SOURCE1} %{buildroot}%{_rpmmacrodir}/macros.clang-wrap
cargo install --path=. --root=%{buildroot}/%{_libdir}/clang-wrap
ln -sf clang %{buildroot}/%{_libdir}/clang-wrap/bin/clang++

%check
# there's no check

%filetriggerin -p /bin/sh -- %{_bindir}
mkdir -p %{clang_wrap_varlibdir}
while read file; do
    name=$(basename $file)
    case $name in
        clang-[0-9]* | clang++-[0-9]* | clang | clang++)
           ln -sf %{_libdir}/clang-wrap/bin/clang %{clang_wrap_varlibdir}/$name
           ;;
    esac
done

%filetriggerun -p /bin/sh -- %{_bindir}
if [ "$2" -ne 0 ];then
    exit 0
fi
while read file; do
    name=$(basename $file)
    case $name in
        clang-[0-9]* | clang++-[0-9]* | clang | clang++)
            rm -f %{clang_wrap_varlibdir}/$name
            ;;
    esac
done

%post
rm -rf %{clang_wrap_varlibdir}
mkdir -p %{clang_wrap_varlibdir}
for file in `find %{_libdir}/clang-wrap/bin -type f,l | grep -v bin/clang`;do
    ln -sf $file %{clang_wrap_varlibdir}
done
for file in `ls %{_bindir}/clang* 2>/dev/null`;do
    name=$(basename $file)
    case $name in
        clang-[0-9]* | clang++-[0-9]* | clang | clang++)
           ln -sf clang %{clang_wrap_varlibdir}/$name
           ;;
    esac
done

%files
%{_libdir}/clang-wrap
%{_rpmmacrodir}/macros.clang-wrap

%changelog
%autochangelog
