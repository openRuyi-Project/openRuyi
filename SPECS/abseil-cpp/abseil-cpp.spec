# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           abseil-cpp
Version:        20260107.0
Release:        %autorelease
Summary:        C++ Common Libraries
License:        Apache-2.0 AND LicenseRef-openRuyi-Public-Domain
URL:            https://abseil.io
VCS:            git:https://github.com/abseil/abseil-cpp
#!RemoteAsset:  sha256:4c124408da902be896a2f368042729655709db5e3004ec99f57e3e14439bc1b2
Source:         https://github.com/abseil/abseil-cpp/archive/%{version}/abseil-cpp-%{version}.tar.gz
BuildSystem:    cmake

# Fix std::bind-backed absl::Condition with GCC 16's libstdc++.
Patch0:         0001-synchronization-accept-general-nullary-functors.patch

BuildRequires:  cmake
BuildRequires:  ninja
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(gmock)
BuildRequires:  pkgconfig(gtest)

BuildOption(conf):  -GNinja
BuildOption(conf):  -DABSL_USE_EXTERNAL_GOOGLETEST:BOOL=ON
BuildOption(conf):  -DABSL_FIND_GOOGLETEST:BOOL=ON
BuildOption(conf):  -DABSL_ENABLE_INSTALL:BOOL=ON
BuildOption(conf):  -DABSL_BUILD_TESTING:BOOL=ON
BuildOption(conf):  -DABSL_BUILD_TEST_HELPERS:BOOL=ON
BuildOption(conf):  -DCMAKE_BUILD_TYPE:STRING=None
BuildOption(conf):  -DCMAKE_CXX_STANDARD:STRING=17
# TODO: Exclude flaky test. https://github.com/abseil/abseil-cpp/issues/1804
BuildOption(check):  --exclude-regex absl_failure_signal_handler_test

# The contents of absl/time/internal/cctz are derived from
# https://github.com/google/cctz (https://src.fedoraproject.org/rpms/cctz), but
# have been forked with Abseil-specific changes. It is not obvious from which
# particular version of CCTZ these sources are derived. Upstream was asked
# about a path to supporting a system copy as required by bundling guidelines:
#   Please comment on CCTZ bundling
#   https://github.com/abseil/abseil-cpp/discussions/1415
# They refused, for the time being, as follows:
#   “[…] we have no plans to change this decision, but we reserve the right to
#   change our minds.”
Provides:       bundled(cctz)

%description
Abseil is an open-source collection of C++ library code designed to augment
the C++ standard library. The Abseil library code is collected from
Google's own C++ code base, has been extensively tested and used in
production, and is the same code we depend on in our daily coding lives.

In some cases, Abseil provides pieces missing from the C++ standard; in
others, Abseil provides alternatives to the standard for special needs we've
found through usage in the Google code base. We denote those cases clearly
within the library code we provide you.

Abseil is not meant to be a competitor to the standard library; we've just
found that many of these utilities serve a purpose within our code base,
and we now want to provide those resources to the C++ community as a whole.

%package        testing
Summary:        Libraries needed for running tests on the installed %{name}
Requires:       %{name} = %{version}-%{release}

Provides:       bundled(cctz)

%description    testing
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-testing = %{version}-%{release}

# Some of the headers from CCTZ are part of the -devel subpackage. See the
# corresponding virtual Provides in the base package for full details.
Provides:       bundled(cctz)

%description    devel
Development headers for %{name}

%files
%global lib_version 2601.0.0
%license LICENSE
%doc FAQ.md README.md UPGRADES.md
# All shared libraries except installed TESTONLY libraries; see the %%files
# list for the -testing subpackage for those.
%{_libdir}/libabsl_base.so.%{lib_version}
%{_libdir}/libabsl_city.so.%{lib_version}
%{_libdir}/libabsl_civil_time.so.%{lib_version}
%{_libdir}/libabsl_cord.so.%{lib_version}
%{_libdir}/libabsl_cord_internal.so.%{lib_version}
%{_libdir}/libabsl_cordz_functions.so.%{lib_version}
%{_libdir}/libabsl_cordz_handle.so.%{lib_version}
%{_libdir}/libabsl_cordz_info.so.%{lib_version}
%{_libdir}/libabsl_cordz_sample_token.so.%{lib_version}
%{_libdir}/libabsl_crc32c.so.%{lib_version}
%{_libdir}/libabsl_crc_cord_state.so.%{lib_version}
%{_libdir}/libabsl_crc_cpu_detect.so.%{lib_version}
%{_libdir}/libabsl_crc_internal.so.%{lib_version}
%{_libdir}/libabsl_debugging_internal.so.%{lib_version}
%{_libdir}/libabsl_decode_rust_punycode.so.%{lib_version}
%{_libdir}/libabsl_demangle_internal.so.%{lib_version}
%{_libdir}/libabsl_demangle_rust.so.%{lib_version}
%{_libdir}/libabsl_die_if_null.so.%{lib_version}
%{_libdir}/libabsl_examine_stack.so.%{lib_version}
%{_libdir}/libabsl_exponential_biased.so.%{lib_version}
%{_libdir}/libabsl_failure_signal_handler.so.%{lib_version}
%{_libdir}/libabsl_flags_commandlineflag.so.%{lib_version}
%{_libdir}/libabsl_flags_commandlineflag_internal.so.%{lib_version}
%{_libdir}/libabsl_flags_config.so.%{lib_version}
%{_libdir}/libabsl_flags_internal.so.%{lib_version}
%{_libdir}/libabsl_flags_marshalling.so.%{lib_version}
%{_libdir}/libabsl_flags_parse.so.%{lib_version}
%{_libdir}/libabsl_flags_private_handle_accessor.so.%{lib_version}
%{_libdir}/libabsl_flags_program_name.so.%{lib_version}
%{_libdir}/libabsl_flags_reflection.so.%{lib_version}
%{_libdir}/libabsl_flags_usage.so.%{lib_version}
%{_libdir}/libabsl_flags_usage_internal.so.%{lib_version}
%{_libdir}/libabsl_graphcycles_internal.so.%{lib_version}
%{_libdir}/libabsl_hash.so.%{lib_version}
%{_libdir}/libabsl_hashtable_profiler.so.%{lib_version}
%{_libdir}/libabsl_hashtablez_sampler.so.%{lib_version}
%{_libdir}/libabsl_int128.so.%{lib_version}
%{_libdir}/libabsl_kernel_timeout_internal.so.%{lib_version}
%{_libdir}/libabsl_leak_check.so.%{lib_version}
%{_libdir}/libabsl_log_flags.so.%{lib_version}
%{_libdir}/libabsl_log_globals.so.%{lib_version}
%{_libdir}/libabsl_log_initialize.so.%{lib_version}
%{_libdir}/libabsl_log_internal_check_op.so.%{lib_version}
%{_libdir}/libabsl_log_internal_conditions.so.%{lib_version}
%{_libdir}/libabsl_log_internal_fnmatch.so.%{lib_version}
%{_libdir}/libabsl_log_internal_format.so.%{lib_version}
%{_libdir}/libabsl_log_internal_globals.so.%{lib_version}
%{_libdir}/libabsl_log_internal_log_sink_set.so.%{lib_version}
%{_libdir}/libabsl_log_internal_message.so.%{lib_version}
%{_libdir}/libabsl_log_internal_nullguard.so.%{lib_version}
%{_libdir}/libabsl_log_internal_proto.so.%{lib_version}
%{_libdir}/libabsl_log_internal_structured_proto.so.%{lib_version}
%{_libdir}/libabsl_log_severity.so.%{lib_version}
%{_libdir}/libabsl_log_sink.so.%{lib_version}
%{_libdir}/libabsl_log_entry.so.%{lib_version}
%{_libdir}/libabsl_malloc_internal.so.%{lib_version}
%{_libdir}/libabsl_periodic_sampler.so.%{lib_version}
%{_libdir}/libabsl_poison.so.%{lib_version}
%{_libdir}/libabsl_profile_builder.so.%{lib_version}
%{_libdir}/libabsl_random_distributions.so.%{lib_version}
%{_libdir}/libabsl_random_internal_distribution_test_util.so.%{lib_version}
%{_libdir}/libabsl_random_internal_entropy_pool.so.%{lib_version}
%{_libdir}/libabsl_random_internal_platform.so.%{lib_version}
%{_libdir}/libabsl_random_internal_randen.so.%{lib_version}
%{_libdir}/libabsl_random_internal_randen_hwaes.so.%{lib_version}
%{_libdir}/libabsl_random_internal_randen_hwaes_impl.so.%{lib_version}
%{_libdir}/libabsl_random_internal_randen_slow.so.%{lib_version}
%{_libdir}/libabsl_random_internal_seed_material.so.%{lib_version}
%{_libdir}/libabsl_random_seed_gen_exception.so.%{lib_version}
%{_libdir}/libabsl_random_seed_sequences.so.%{lib_version}
%{_libdir}/libabsl_raw_hash_set.so.%{lib_version}
%{_libdir}/libabsl_raw_logging_internal.so.%{lib_version}
%{_libdir}/libabsl_scoped_set_env.so.%{lib_version}
%{_libdir}/libabsl_spinlock_wait.so.%{lib_version}
%{_libdir}/libabsl_stacktrace.so.%{lib_version}
%{_libdir}/libabsl_status.so.%{lib_version}
%{_libdir}/libabsl_statusor.so.%{lib_version}
%{_libdir}/libabsl_str_format_internal.so.%{lib_version}
%{_libdir}/libabsl_strerror.so.%{lib_version}
%{_libdir}/libabsl_strings.so.%{lib_version}
%{_libdir}/libabsl_strings_internal.so.%{lib_version}
%{_libdir}/libabsl_borrowed_fixup_buffer.so.%{lib_version}
%{_libdir}/libabsl_generic_printer_internal.so.%{lib_version}
%{_libdir}/libabsl_symbolize.so.%{lib_version}
%{_libdir}/libabsl_synchronization.so.%{lib_version}
%{_libdir}/libabsl_throw_delegate.so.%{lib_version}
%{_libdir}/libabsl_time.so.%{lib_version}
%{_libdir}/libabsl_time_zone.so.%{lib_version}
%{_libdir}/libabsl_tracing_internal.so.%{lib_version}
%{_libdir}/libabsl_utf8_for_code_point.so.%{lib_version}
%{_libdir}/libabsl_vlog_config_internal.so.%{lib_version}

%files testing
# TESTONLY libraries (that are actually installed):
# absl/base/CMakeLists.txt
%{_libdir}/libabsl_exception_safety_testing.so.%{lib_version}
%{_libdir}/libabsl_atomic_hook_test_helper.so.%{lib_version}
%{_libdir}/libabsl_spinlock_test_common.so.%{lib_version}
# absl/container/CMakeLists.txt
%{_libdir}/libabsl_test_instance_tracker.so.%{lib_version}
%{_libdir}/libabsl_hash_generator_testing.so.%{lib_version}
# absl/debugging/CMakeLists.txt
%{_libdir}/libabsl_stack_consumption.so.%{lib_version}
# absl/log/CMakeLists.txt
%{_libdir}/libabsl_log_internal_test_actions.so.%{lib_version}
%{_libdir}/libabsl_log_internal_test_helpers.so.%{lib_version}
%{_libdir}/libabsl_log_internal_test_matchers.so.%{lib_version}
%{_libdir}/libabsl_scoped_mock_log.so.%{lib_version}
# absl/status/CMakeLists.txt
%{_libdir}/libabsl_status_matchers.so.%{lib_version}
# absl/strings/CMakeLists.txt
%{_libdir}/libabsl_pow10_helper.so.%{lib_version}
# absl/synchronization/CMakeLists.txt
%{_libdir}/libabsl_per_thread_sem_test_common.so.%{lib_version}
# absl/time/CMakeLists.txt
%{_libdir}/libabsl_time_internal_test_util.so.%{lib_version}

%files devel
%{_includedir}/absl
%{_libdir}/libabsl_*.so
%{_libdir}/cmake/absl
%{_libdir}/pkgconfig/absl_absl_check.pc
%{_libdir}/pkgconfig/absl_absl_log.pc
%{_libdir}/pkgconfig/absl_absl_vlog_is_on.pc
%{_libdir}/pkgconfig/absl_algorithm.pc
%{_libdir}/pkgconfig/absl_algorithm_container.pc
%{_libdir}/pkgconfig/absl_any.pc
%{_libdir}/pkgconfig/absl_any_invocable.pc
%{_libdir}/pkgconfig/absl_atomic_hook.pc
%{_libdir}/pkgconfig/absl_atomic_hook_test_helper.pc
%{_libdir}/pkgconfig/absl_bad_any_cast.pc
%{_libdir}/pkgconfig/absl_bad_optional_access.pc
%{_libdir}/pkgconfig/absl_bad_variant_access.pc
%{_libdir}/pkgconfig/absl_base.pc
%{_libdir}/pkgconfig/absl_base_internal.pc
%{_libdir}/pkgconfig/absl_bind_front.pc
%{_libdir}/pkgconfig/absl_bits.pc
%{_libdir}/pkgconfig/absl_borrowed_fixup_buffer.pc
%{_libdir}/pkgconfig/absl_bounded_utf8_length_sequence.pc
%{_libdir}/pkgconfig/absl_btree.pc
%{_libdir}/pkgconfig/absl_btree_test_common.pc
%{_libdir}/pkgconfig/absl_charset.pc
%{_libdir}/pkgconfig/absl_check.pc
%{_libdir}/pkgconfig/absl_chunked_queue.pc
%{_libdir}/pkgconfig/absl_city.pc
%{_libdir}/pkgconfig/absl_civil_time.pc
%{_libdir}/pkgconfig/absl_cleanup.pc
%{_libdir}/pkgconfig/absl_cleanup_internal.pc
%{_libdir}/pkgconfig/absl_common_policy_traits.pc
%{_libdir}/pkgconfig/absl_compare.pc
%{_libdir}/pkgconfig/absl_compressed_tuple.pc
%{_libdir}/pkgconfig/absl_config.pc
%{_libdir}/pkgconfig/absl_constexpr_testing_internal.pc
%{_libdir}/pkgconfig/absl_container_common.pc
%{_libdir}/pkgconfig/absl_container_memory.pc
%{_libdir}/pkgconfig/absl_cord.pc
%{_libdir}/pkgconfig/absl_cord_internal.pc
%{_libdir}/pkgconfig/absl_cord_rep_test_util.pc
%{_libdir}/pkgconfig/absl_cord_test_helpers.pc
%{_libdir}/pkgconfig/absl_cordz_functions.pc
%{_libdir}/pkgconfig/absl_cordz_handle.pc
%{_libdir}/pkgconfig/absl_cordz_info.pc
%{_libdir}/pkgconfig/absl_cordz_sample_token.pc
%{_libdir}/pkgconfig/absl_cordz_statistics.pc
%{_libdir}/pkgconfig/absl_cordz_test_helpers.pc
%{_libdir}/pkgconfig/absl_cordz_update_scope.pc
%{_libdir}/pkgconfig/absl_cordz_update_tracker.pc
%{_libdir}/pkgconfig/absl_core_headers.pc
%{_libdir}/pkgconfig/absl_crc32c.pc
%{_libdir}/pkgconfig/absl_crc_cord_state.pc
%{_libdir}/pkgconfig/absl_crc_cpu_detect.pc
%{_libdir}/pkgconfig/absl_crc_internal.pc
%{_libdir}/pkgconfig/absl_debugging.pc
%{_libdir}/pkgconfig/absl_debugging_internal.pc
%{_libdir}/pkgconfig/absl_decode_rust_punycode.pc
%{_libdir}/pkgconfig/absl_demangle_internal.pc
%{_libdir}/pkgconfig/absl_demangle_rust.pc
%{_libdir}/pkgconfig/absl_die_if_null.pc
%{_libdir}/pkgconfig/absl_dynamic_annotations.pc
%{_libdir}/pkgconfig/absl_endian.pc
%{_libdir}/pkgconfig/absl_errno_saver.pc
%{_libdir}/pkgconfig/absl_examine_stack.pc
%{_libdir}/pkgconfig/absl_exception_safety_testing.pc
%{_libdir}/pkgconfig/absl_exception_testing.pc
%{_libdir}/pkgconfig/absl_exponential_biased.pc
%{_libdir}/pkgconfig/absl_failure_signal_handler.pc
%{_libdir}/pkgconfig/absl_fast_type_id.pc
%{_libdir}/pkgconfig/absl_fixed_array.pc
%{_libdir}/pkgconfig/absl_flags.pc
%{_libdir}/pkgconfig/absl_flags_commandlineflag.pc
%{_libdir}/pkgconfig/absl_flags_commandlineflag_internal.pc
%{_libdir}/pkgconfig/absl_flags_config.pc
%{_libdir}/pkgconfig/absl_flags_internal.pc
%{_libdir}/pkgconfig/absl_flags_marshalling.pc
%{_libdir}/pkgconfig/absl_flags_parse.pc
%{_libdir}/pkgconfig/absl_flags_path_util.pc
%{_libdir}/pkgconfig/absl_flags_private_handle_accessor.pc
%{_libdir}/pkgconfig/absl_flags_program_name.pc
%{_libdir}/pkgconfig/absl_flags_reflection.pc
%{_libdir}/pkgconfig/absl_flags_usage.pc
%{_libdir}/pkgconfig/absl_flags_usage_internal.pc
%{_libdir}/pkgconfig/absl_flat_hash_map.pc
%{_libdir}/pkgconfig/absl_flat_hash_set.pc
%{_libdir}/pkgconfig/absl_function_ref.pc
%{_libdir}/pkgconfig/absl_generic_printer_internal.pc
%{_libdir}/pkgconfig/absl_graphcycles_internal.pc
%{_libdir}/pkgconfig/absl_has_ostream_operator.pc
%{_libdir}/pkgconfig/absl_hash.pc
%{_libdir}/pkgconfig/absl_hash_container_defaults.pc
%{_libdir}/pkgconfig/absl_hash_function_defaults.pc
%{_libdir}/pkgconfig/absl_hash_generator_testing.pc
%{_libdir}/pkgconfig/absl_hash_policy_testing.pc
%{_libdir}/pkgconfig/absl_hash_policy_traits.pc
%{_libdir}/pkgconfig/absl_hash_testing.pc
%{_libdir}/pkgconfig/absl_hashtable_control_bytes.pc
%{_libdir}/pkgconfig/absl_hashtable_debug.pc
%{_libdir}/pkgconfig/absl_hashtable_debug_hooks.pc
%{_libdir}/pkgconfig/absl_hashtable_profiler.pc
%{_libdir}/pkgconfig/absl_hashtablez_sampler.pc
%{_libdir}/pkgconfig/absl_heterogeneous_lookup_testing.pc
%{_libdir}/pkgconfig/absl_inlined_vector.pc
%{_libdir}/pkgconfig/absl_inlined_vector_internal.pc
%{_libdir}/pkgconfig/absl_int128.pc
%{_libdir}/pkgconfig/absl_iterator_traits_internal.pc
%{_libdir}/pkgconfig/absl_iterator_traits_test_helper_internal.pc
%{_libdir}/pkgconfig/absl_kernel_timeout_internal.pc
%{_libdir}/pkgconfig/absl_layout.pc
%{_libdir}/pkgconfig/absl_leak_check.pc
%{_libdir}/pkgconfig/absl_linked_hash_map.pc
%{_libdir}/pkgconfig/absl_linked_hash_set.pc
%{_libdir}/pkgconfig/absl_log.pc
%{_libdir}/pkgconfig/absl_log_entry.pc
%{_libdir}/pkgconfig/absl_log_flags.pc
%{_libdir}/pkgconfig/absl_log_globals.pc
%{_libdir}/pkgconfig/absl_log_initialize.pc
%{_libdir}/pkgconfig/absl_log_internal_append_truncated.pc
%{_libdir}/pkgconfig/absl_log_internal_check_impl.pc
%{_libdir}/pkgconfig/absl_log_internal_check_op.pc
%{_libdir}/pkgconfig/absl_log_internal_conditions.pc
%{_libdir}/pkgconfig/absl_log_internal_config.pc
%{_libdir}/pkgconfig/absl_log_internal_container.pc
%{_libdir}/pkgconfig/absl_log_internal_flags.pc
%{_libdir}/pkgconfig/absl_log_internal_fnmatch.pc
%{_libdir}/pkgconfig/absl_log_internal_format.pc
%{_libdir}/pkgconfig/absl_log_internal_globals.pc
%{_libdir}/pkgconfig/absl_log_internal_log_impl.pc
%{_libdir}/pkgconfig/absl_log_internal_log_sink_set.pc
%{_libdir}/pkgconfig/absl_log_internal_message.pc
%{_libdir}/pkgconfig/absl_log_internal_nullguard.pc
%{_libdir}/pkgconfig/absl_log_internal_nullstream.pc
%{_libdir}/pkgconfig/absl_log_internal_proto.pc
%{_libdir}/pkgconfig/absl_log_internal_strip.pc
%{_libdir}/pkgconfig/absl_log_internal_structured.pc
%{_libdir}/pkgconfig/absl_log_internal_structured_proto.pc
%{_libdir}/pkgconfig/absl_log_internal_test_actions.pc
%{_libdir}/pkgconfig/absl_log_internal_test_helpers.pc
%{_libdir}/pkgconfig/absl_log_internal_test_matchers.pc
%{_libdir}/pkgconfig/absl_log_internal_voidify.pc
%{_libdir}/pkgconfig/absl_log_severity.pc
%{_libdir}/pkgconfig/absl_log_sink.pc
%{_libdir}/pkgconfig/absl_log_sink_registry.pc
%{_libdir}/pkgconfig/absl_log_streamer.pc
%{_libdir}/pkgconfig/absl_log_structured.pc
%{_libdir}/pkgconfig/absl_malloc_internal.pc
%{_libdir}/pkgconfig/absl_memory.pc
%{_libdir}/pkgconfig/absl_meta.pc
%{_libdir}/pkgconfig/absl_no_destructor.pc
%{_libdir}/pkgconfig/absl_node_hash_map.pc
%{_libdir}/pkgconfig/absl_node_hash_set.pc
%{_libdir}/pkgconfig/absl_node_slot_policy.pc
%{_libdir}/pkgconfig/absl_non_temporal_arm_intrinsics.pc
%{_libdir}/pkgconfig/absl_non_temporal_memcpy.pc
%{_libdir}/pkgconfig/absl_nullability.pc
%{_libdir}/pkgconfig/absl_nullability_traits_internal.pc
%{_libdir}/pkgconfig/absl_numeric.pc
%{_libdir}/pkgconfig/absl_numeric_representation.pc
%{_libdir}/pkgconfig/absl_optional.pc
%{_libdir}/pkgconfig/absl_overload.pc
%{_libdir}/pkgconfig/absl_per_thread_sem_test_common.pc
%{_libdir}/pkgconfig/absl_periodic_sampler.pc
%{_libdir}/pkgconfig/absl_poison.pc
%{_libdir}/pkgconfig/absl_pow10_helper.pc
%{_libdir}/pkgconfig/absl_prefetch.pc
%{_libdir}/pkgconfig/absl_pretty_function.pc
%{_libdir}/pkgconfig/absl_profile_builder.pc
%{_libdir}/pkgconfig/absl_random_bit_gen_ref.pc
%{_libdir}/pkgconfig/absl_random_distributions.pc
%{_libdir}/pkgconfig/absl_random_internal_distribution_caller.pc
%{_libdir}/pkgconfig/absl_random_internal_distribution_test_util.pc
%{_libdir}/pkgconfig/absl_random_internal_entropy_pool.pc
%{_libdir}/pkgconfig/absl_random_internal_explicit_seed_seq.pc
%{_libdir}/pkgconfig/absl_random_internal_fast_uniform_bits.pc
%{_libdir}/pkgconfig/absl_random_internal_fastmath.pc
%{_libdir}/pkgconfig/absl_random_internal_generate_real.pc
%{_libdir}/pkgconfig/absl_random_internal_iostream_state_saver.pc
%{_libdir}/pkgconfig/absl_random_internal_mock_helpers.pc
%{_libdir}/pkgconfig/absl_random_internal_mock_overload_set.pc
%{_libdir}/pkgconfig/absl_random_internal_mock_validators.pc
%{_libdir}/pkgconfig/absl_random_internal_nonsecure_base.pc
%{_libdir}/pkgconfig/absl_random_internal_pcg_engine.pc
%{_libdir}/pkgconfig/absl_random_internal_platform.pc
%{_libdir}/pkgconfig/absl_random_internal_randen.pc
%{_libdir}/pkgconfig/absl_random_internal_randen_engine.pc
%{_libdir}/pkgconfig/absl_random_internal_randen_hwaes.pc
%{_libdir}/pkgconfig/absl_random_internal_randen_hwaes_impl.pc
%{_libdir}/pkgconfig/absl_random_internal_randen_slow.pc
%{_libdir}/pkgconfig/absl_random_internal_salted_seed_seq.pc
%{_libdir}/pkgconfig/absl_random_internal_seed_material.pc
%{_libdir}/pkgconfig/absl_random_internal_sequence_urbg.pc
%{_libdir}/pkgconfig/absl_random_internal_traits.pc
%{_libdir}/pkgconfig/absl_random_internal_uniform_helper.pc
%{_libdir}/pkgconfig/absl_random_internal_wide_multiply.pc
%{_libdir}/pkgconfig/absl_random_mocking_bit_gen.pc
%{_libdir}/pkgconfig/absl_random_random.pc
%{_libdir}/pkgconfig/absl_random_seed_gen_exception.pc
%{_libdir}/pkgconfig/absl_random_seed_sequences.pc
%{_libdir}/pkgconfig/absl_raw_hash_map.pc
%{_libdir}/pkgconfig/absl_raw_hash_set.pc
%{_libdir}/pkgconfig/absl_raw_hash_set_resize_impl.pc
%{_libdir}/pkgconfig/absl_raw_logging_internal.pc
%{_libdir}/pkgconfig/absl_requires_internal.pc
%{_libdir}/pkgconfig/absl_sample_recorder.pc
%{_libdir}/pkgconfig/absl_scoped_mock_log.pc
%{_libdir}/pkgconfig/absl_scoped_set_env.pc
%{_libdir}/pkgconfig/absl_span.pc
%{_libdir}/pkgconfig/absl_spinlock_test_common.pc
%{_libdir}/pkgconfig/absl_spinlock_wait.pc
%{_libdir}/pkgconfig/absl_spy_hash_state.pc
%{_libdir}/pkgconfig/absl_stack_consumption.pc
%{_libdir}/pkgconfig/absl_stacktrace.pc
%{_libdir}/pkgconfig/absl_status.pc
%{_libdir}/pkgconfig/absl_status_matchers.pc
%{_libdir}/pkgconfig/absl_statusor.pc
%{_libdir}/pkgconfig/absl_str_format.pc
%{_libdir}/pkgconfig/absl_str_format_internal.pc
%{_libdir}/pkgconfig/absl_strerror.pc
%{_libdir}/pkgconfig/absl_string_view.pc
%{_libdir}/pkgconfig/absl_strings.pc
%{_libdir}/pkgconfig/absl_strings_append_and_overwrite.pc
%{_libdir}/pkgconfig/absl_strings_internal.pc
%{_libdir}/pkgconfig/absl_strings_resize_and_overwrite.pc
%{_libdir}/pkgconfig/absl_symbolize.pc
%{_libdir}/pkgconfig/absl_synchronization.pc
%{_libdir}/pkgconfig/absl_test_allocator.pc
%{_libdir}/pkgconfig/absl_test_instance_tracker.pc
%{_libdir}/pkgconfig/absl_thread_pool.pc
%{_libdir}/pkgconfig/absl_throw_delegate.pc
%{_libdir}/pkgconfig/absl_time.pc
%{_libdir}/pkgconfig/absl_time_internal_test_util.pc
%{_libdir}/pkgconfig/absl_time_zone.pc
%{_libdir}/pkgconfig/absl_tracing_internal.pc
%{_libdir}/pkgconfig/absl_tracked.pc
%{_libdir}/pkgconfig/absl_type_traits.pc
%{_libdir}/pkgconfig/absl_unordered_map_constructor_test.pc
%{_libdir}/pkgconfig/absl_unordered_map_lookup_test.pc
%{_libdir}/pkgconfig/absl_unordered_map_members_test.pc
%{_libdir}/pkgconfig/absl_unordered_map_modifiers_test.pc
%{_libdir}/pkgconfig/absl_unordered_set_constructor_test.pc
%{_libdir}/pkgconfig/absl_unordered_set_lookup_test.pc
%{_libdir}/pkgconfig/absl_unordered_set_members_test.pc
%{_libdir}/pkgconfig/absl_unordered_set_modifiers_test.pc
%{_libdir}/pkgconfig/absl_utf8_for_code_point.pc
%{_libdir}/pkgconfig/absl_utility.pc
%{_libdir}/pkgconfig/absl_variant.pc
%{_libdir}/pkgconfig/absl_vlog_config_internal.pc
%{_libdir}/pkgconfig/absl_vlog_is_on.pc
%{_libdir}/pkgconfig/absl_weakly_mixed_integer.pc

%changelog
%autochangelog
