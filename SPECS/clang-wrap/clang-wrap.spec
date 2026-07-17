# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: YunQiang Su <yunqiang@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global git_ver git20260717.b329f3b
%global git_commit b329f3b109d4ef2d82a0506929d5dd92448bfb79

Name:           clang-wrap
Version:        0+%{git_ver}
Release:        %{autorelease}
License:        Mulan-2.0
Summary:        clang-wrap to collect LLVM IR
URL:            https://github.com/openRuyi-Project/clang-wrap
#!RemoteAsset:  sha256:3c26fe2ef147b34e64b4f2e02301d75cb2652f7b627aa6afd49e83e66cea910f
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
    name=$(basename "$file")
    case "$name" in
        clang-[0-9]* | clang++-[0-9]* | clang | clang++)
            ln -sf %{_libdir}/clang-wrap/bin/clang %{clang_wrap_varlibdir}/$name
            ;;
        clang*)
            ;;
        *)
            if [ -e "%{_libdir}/clang-wrap/bin/$name" ]; then
                ln -sf %{_libdir}/clang-wrap/bin/$name %{clang_wrap_varlibdir}/$name
            fi
           ;;
    esac
done

%filetriggerun -p /bin/sh -- %{_bindir}
if [ "$2" -ne 0 ];then
    exit 0
fi
while read file; do
    name=$(basename "$file")
    case "$name" in
        clang-[0-9]* | clang++-[0-9]* | clang | clang++)
            rm -f %{clang_wrap_varlibdir}/$name
            ;;
        clang*)
            ;;
        *)
            if [ -e "%{_libdir}/clang-wrap/bin/$name" ]; then
                rm -f %{clang_wrap_varlibdir}/$name
            fi
            ;;
    esac
done

%post
rm -rf %{clang_wrap_varlibdir}
mkdir -p %{clang_wrap_varlibdir}
for file in %{_libdir}/clang-wrap/bin/*; do
    [ -e "$file" ] || continue
    name=$(basename "$file")
    case "$name" in
        clang*)
            ;;
        *)
            if [ -e "%{_bindir}/$name" ]; then
                ln -sf $file %{clang_wrap_varlibdir}/$name
            fi
            ;;
    esac
done
for file in %{_bindir}/clang*; do
    [ -e "$file" ] || continue
    name=$(basename "$file")
    case "$name" in
        clang-[0-9]* | clang++-[0-9]* | clang | clang++)
            ln -sf %{_libdir}/clang-wrap/bin/clang %{clang_wrap_varlibdir}/$name
           ;;
    esac
done

%postun
if [ $1 -eq 0 ]; then
    rm -rf %{clang_wrap_varlibdir}
fi

%files
%{_libdir}/clang-wrap
%{_rpmmacrodir}/macros.clang-wrap

%changelog
%autochangelog
