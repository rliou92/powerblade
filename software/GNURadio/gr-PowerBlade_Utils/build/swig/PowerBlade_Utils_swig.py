# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.11
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_PowerBlade_Utils_swig', [dirname(__file__)])
        except ImportError:
            import _PowerBlade_Utils_swig
            return _PowerBlade_Utils_swig
        if fp is not None:
            try:
                _mod = imp.load_module('_PowerBlade_Utils_swig', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _PowerBlade_Utils_swig = swig_import_helper()
    del swig_import_helper
else:
    import _PowerBlade_Utils_swig
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


def _swig_setattr_nondynamic_method(set):
    def set_attr(self,name,value):
        if (name == "thisown"): return self.this.own(value)
        if hasattr(self,name) or (name == "this"):
            set(self,name,value)
        else:
            raise AttributeError("You cannot add attributes to %s" % self)
    return set_attr



def high_res_timer_now():
  """high_res_timer_now() -> gr::high_res_timer_type"""
  return _PowerBlade_Utils_swig.high_res_timer_now()

def high_res_timer_now_perfmon():
  """high_res_timer_now_perfmon() -> gr::high_res_timer_type"""
  return _PowerBlade_Utils_swig.high_res_timer_now_perfmon()

def high_res_timer_tps():
  """high_res_timer_tps() -> gr::high_res_timer_type"""
  return _PowerBlade_Utils_swig.high_res_timer_tps()

def high_res_timer_epoch():
  """high_res_timer_epoch() -> gr::high_res_timer_type"""
  return _PowerBlade_Utils_swig.high_res_timer_epoch()
class ByteToPseudoUARTi(object):
    """Takes bytes being sent in and converts them into a series of 0 and 1 samples that represent the UART encoding of the thing."""
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    def make(*args, **kwargs):
        """
        make(uint8_t withTimingBit, uint8_t rearPaddingBits, uint8_t rearPauseBits, uint8_t symbolsPerBlock, 
            uint32_t blockPause) -> ByteToPseudoUARTi_sptr

        Return a shared_ptr to a new instance of PowerBlade_Utils::ByteToPseudoUARTi.

        To avoid accidental use of raw pointers, PowerBlade_Utils::ByteToPseudoUARTi's constructor is in a private implementation class. PowerBlade_Utils::ByteToPseudoUARTi::make is the public interface for creating new instances.

        Params: (withTimingBit, rearPaddingBits, rearPauseBits, symbolsPerBlock, blockPause)
        """
        return _PowerBlade_Utils_swig.ByteToPseudoUARTi_make(*args, **kwargs)

    make = staticmethod(make)
    __swig_destroy__ = _PowerBlade_Utils_swig.delete_ByteToPseudoUARTi
    __del__ = lambda self : None;
ByteToPseudoUARTi_swigregister = _PowerBlade_Utils_swig.ByteToPseudoUARTi_swigregister
ByteToPseudoUARTi_swigregister(ByteToPseudoUARTi)

def ByteToPseudoUARTi_make(*args, **kwargs):
  """
    ByteToPseudoUARTi_make(uint8_t withTimingBit, uint8_t rearPaddingBits, uint8_t rearPauseBits, uint8_t symbolsPerBlock, 
        uint32_t blockPause) -> ByteToPseudoUARTi_sptr

    Return a shared_ptr to a new instance of PowerBlade_Utils::ByteToPseudoUARTi.

    To avoid accidental use of raw pointers, PowerBlade_Utils::ByteToPseudoUARTi's constructor is in a private implementation class. PowerBlade_Utils::ByteToPseudoUARTi::make is the public interface for creating new instances.

    Params: (withTimingBit, rearPaddingBits, rearPauseBits, symbolsPerBlock, blockPause)
    """
  return _PowerBlade_Utils_swig.ByteToPseudoUARTi_make(*args, **kwargs)

class ByteToPseudoUARTi_sptr(object):
    """Proxy of C++ boost::shared_ptr<(gr::PowerBlade_Utils::ByteToPseudoUARTi)> class"""
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(boost::shared_ptr<(gr::PowerBlade_Utils::ByteToPseudoUARTi)> self) -> ByteToPseudoUARTi_sptr
        __init__(boost::shared_ptr<(gr::PowerBlade_Utils::ByteToPseudoUARTi)> self, ByteToPseudoUARTi p) -> ByteToPseudoUARTi_sptr
        """
        this = _PowerBlade_Utils_swig.new_ByteToPseudoUARTi_sptr(*args)
        try: self.this.append(this)
        except: self.this = this
    def __deref__(self):
        """__deref__(ByteToPseudoUARTi_sptr self) -> ByteToPseudoUARTi"""
        return _PowerBlade_Utils_swig.ByteToPseudoUARTi_sptr___deref__(self)

    __swig_destroy__ = _PowerBlade_Utils_swig.delete_ByteToPseudoUARTi_sptr
    __del__ = lambda self : None;
    def make(self, *args, **kwargs):
        """
        make(ByteToPseudoUARTi_sptr self, uint8_t withTimingBit, uint8_t rearPaddingBits, uint8_t rearPauseBits, uint8_t symbolsPerBlock, 
            uint32_t blockPause) -> ByteToPseudoUARTi_sptr

        Return a shared_ptr to a new instance of PowerBlade_Utils::ByteToPseudoUARTi.

        To avoid accidental use of raw pointers, PowerBlade_Utils::ByteToPseudoUARTi's constructor is in a private implementation class. PowerBlade_Utils::ByteToPseudoUARTi::make is the public interface for creating new instances.

        Params: (withTimingBit, rearPaddingBits, rearPauseBits, symbolsPerBlock, blockPause)
        """
        return _PowerBlade_Utils_swig.ByteToPseudoUARTi_sptr_make(self, *args, **kwargs)

    def history(self):
        """history(ByteToPseudoUARTi_sptr self) -> unsigned int"""
        return _PowerBlade_Utils_swig.ByteToPseudoUARTi_sptr_history(self)

    def declare_sample_delay(self, *args):
        """
        declare_sample_delay(ByteToPseudoUARTi_sptr self, int which, int delay)
        declare_sample_delay(ByteToPseudoUARTi_sptr self, unsigned int delay)
        """
        return _PowerBlade_Utils_swig.ByteToPseudoUARTi_sptr_declare_sample_delay(self, *args)

    def sample_delay(self, *args, **kwargs):
        """sample_delay(ByteToPseudoUARTi_sptr self, int which) -> unsigned int"""
        return _PowerBlade_Utils_swig.ByteToPseudoUARTi_sptr_sample_delay(self, *args, **kwargs)

    def output_multiple(self):
        """output_multiple(ByteToPseudoUARTi_sptr self) -> int"""
        return _PowerBlade_Utils_swig.ByteToPseudoUARTi_sptr_output_multiple(self)

    def relative_rate(self):
        """relative_rate(ByteToPseudoUARTi_sptr self) -> double"""
        return _PowerBlade_Utils_swig.ByteToPseudoUARTi_sptr_relative_rate(self)

    def start(self):
        """start(ByteToPseudoUARTi_sptr self) -> bool"""
        return _PowerBlade_Utils_swig.ByteToPseudoUARTi_sptr_start(self)

    def stop(self):
        """stop(ByteToPseudoUARTi_sptr self) -> bool"""
        return _PowerBlade_Utils_swig.ByteToPseudoUARTi_sptr_stop(self)

    def nitems_read(self, *args, **kwargs):
        """nitems_read(ByteToPseudoUARTi_sptr self, unsigned int which_input) -> uint64_t"""
        return _PowerBlade_Utils_swig.ByteToPseudoUARTi_sptr_nitems_read(self, *args, **kwargs)

    def nitems_written(self, *args, **kwargs):
        """nitems_written(ByteToPseudoUARTi_sptr self, unsigned int which_output) -> uint64_t"""
        return _PowerBlade_Utils_swig.ByteToPseudoUARTi_sptr_nitems_written(self, *args, **kwargs)

    def max_noutput_items(self):
        """max_noutput_items(ByteToPseudoUARTi_sptr self) -> int"""
        return _PowerBlade_Utils_swig.ByteToPseudoUARTi_sptr_max_noutput_items(self)

    def set_max_noutput_items(self, *args, **kwargs):
        """set_max_noutput_items(ByteToPseudoUARTi_sptr self, int m)"""
        return _PowerBlade_Utils_swig.ByteToPseudoUARTi_sptr_set_max_noutput_items(self, *args, **kwargs)

    def unset_max_noutput_items(self):
        """unset_max_noutput_items(ByteToPseudoUARTi_sptr self)"""
        return _PowerBlade_Utils_swig.ByteToPseudoUARTi_sptr_unset_max_noutput_items(self)

    def is_set_max_noutput_items(self):
        """is_set_max_noutput_items(ByteToPseudoUARTi_sptr self) -> bool"""
        return _PowerBlade_Utils_swig.ByteToPseudoUARTi_sptr_is_set_max_noutput_items(self)

    def max_output_buffer(self, *args, **kwargs):
        """max_output_buffer(ByteToPseudoUARTi_sptr self, int i) -> long"""
        return _PowerBlade_Utils_swig.ByteToPseudoUARTi_sptr_max_output_buffer(self, *args, **kwargs)

    def set_max_output_buffer(self, *args):
        """
        set_max_output_buffer(ByteToPseudoUARTi_sptr self, long max_output_buffer)
        set_max_output_buffer(ByteToPseudoUARTi_sptr self, int port, long max_output_buffer)
        """
        return _PowerBlade_Utils_swig.ByteToPseudoUARTi_sptr_set_max_output_buffer(self, *args)

    def min_output_buffer(self, *args, **kwargs):
        """min_output_buffer(ByteToPseudoUARTi_sptr self, int i) -> long"""
        return _PowerBlade_Utils_swig.ByteToPseudoUARTi_sptr_min_output_buffer(self, *args, **kwargs)

    def set_min_output_buffer(self, *args):
        """
        set_min_output_buffer(ByteToPseudoUARTi_sptr self, long min_output_buffer)
        set_min_output_buffer(ByteToPseudoUARTi_sptr self, int port, long min_output_buffer)
        """
        return _PowerBlade_Utils_swig.ByteToPseudoUARTi_sptr_set_min_output_buffer(self, *args)

    def pc_noutput_items(self):
        """pc_noutput_items(ByteToPseudoUARTi_sptr self) -> float"""
        return _PowerBlade_Utils_swig.ByteToPseudoUARTi_sptr_pc_noutput_items(self)

    def pc_noutput_items_avg(self):
        """pc_noutput_items_avg(ByteToPseudoUARTi_sptr self) -> float"""
        return _PowerBlade_Utils_swig.ByteToPseudoUARTi_sptr_pc_noutput_items_avg(self)

    def pc_noutput_items_var(self):
        """pc_noutput_items_var(ByteToPseudoUARTi_sptr self) -> float"""
        return _PowerBlade_Utils_swig.ByteToPseudoUARTi_sptr_pc_noutput_items_var(self)

    def pc_nproduced(self):
        """pc_nproduced(ByteToPseudoUARTi_sptr self) -> float"""
        return _PowerBlade_Utils_swig.ByteToPseudoUARTi_sptr_pc_nproduced(self)

    def pc_nproduced_avg(self):
        """pc_nproduced_avg(ByteToPseudoUARTi_sptr self) -> float"""
        return _PowerBlade_Utils_swig.ByteToPseudoUARTi_sptr_pc_nproduced_avg(self)

    def pc_nproduced_var(self):
        """pc_nproduced_var(ByteToPseudoUARTi_sptr self) -> float"""
        return _PowerBlade_Utils_swig.ByteToPseudoUARTi_sptr_pc_nproduced_var(self)

    def pc_input_buffers_full(self, *args):
        """
        pc_input_buffers_full(ByteToPseudoUARTi_sptr self, int which) -> float
        pc_input_buffers_full(ByteToPseudoUARTi_sptr self) -> pmt_vector_float
        """
        return _PowerBlade_Utils_swig.ByteToPseudoUARTi_sptr_pc_input_buffers_full(self, *args)

    def pc_input_buffers_full_avg(self, *args):
        """
        pc_input_buffers_full_avg(ByteToPseudoUARTi_sptr self, int which) -> float
        pc_input_buffers_full_avg(ByteToPseudoUARTi_sptr self) -> pmt_vector_float
        """
        return _PowerBlade_Utils_swig.ByteToPseudoUARTi_sptr_pc_input_buffers_full_avg(self, *args)

    def pc_input_buffers_full_var(self, *args):
        """
        pc_input_buffers_full_var(ByteToPseudoUARTi_sptr self, int which) -> float
        pc_input_buffers_full_var(ByteToPseudoUARTi_sptr self) -> pmt_vector_float
        """
        return _PowerBlade_Utils_swig.ByteToPseudoUARTi_sptr_pc_input_buffers_full_var(self, *args)

    def pc_output_buffers_full(self, *args):
        """
        pc_output_buffers_full(ByteToPseudoUARTi_sptr self, int which) -> float
        pc_output_buffers_full(ByteToPseudoUARTi_sptr self) -> pmt_vector_float
        """
        return _PowerBlade_Utils_swig.ByteToPseudoUARTi_sptr_pc_output_buffers_full(self, *args)

    def pc_output_buffers_full_avg(self, *args):
        """
        pc_output_buffers_full_avg(ByteToPseudoUARTi_sptr self, int which) -> float
        pc_output_buffers_full_avg(ByteToPseudoUARTi_sptr self) -> pmt_vector_float
        """
        return _PowerBlade_Utils_swig.ByteToPseudoUARTi_sptr_pc_output_buffers_full_avg(self, *args)

    def pc_output_buffers_full_var(self, *args):
        """
        pc_output_buffers_full_var(ByteToPseudoUARTi_sptr self, int which) -> float
        pc_output_buffers_full_var(ByteToPseudoUARTi_sptr self) -> pmt_vector_float
        """
        return _PowerBlade_Utils_swig.ByteToPseudoUARTi_sptr_pc_output_buffers_full_var(self, *args)

    def pc_work_time(self):
        """pc_work_time(ByteToPseudoUARTi_sptr self) -> float"""
        return _PowerBlade_Utils_swig.ByteToPseudoUARTi_sptr_pc_work_time(self)

    def pc_work_time_avg(self):
        """pc_work_time_avg(ByteToPseudoUARTi_sptr self) -> float"""
        return _PowerBlade_Utils_swig.ByteToPseudoUARTi_sptr_pc_work_time_avg(self)

    def pc_work_time_var(self):
        """pc_work_time_var(ByteToPseudoUARTi_sptr self) -> float"""
        return _PowerBlade_Utils_swig.ByteToPseudoUARTi_sptr_pc_work_time_var(self)

    def pc_work_time_total(self):
        """pc_work_time_total(ByteToPseudoUARTi_sptr self) -> float"""
        return _PowerBlade_Utils_swig.ByteToPseudoUARTi_sptr_pc_work_time_total(self)

    def set_processor_affinity(self, *args, **kwargs):
        """set_processor_affinity(ByteToPseudoUARTi_sptr self, std::vector< int,std::allocator< int > > const & mask)"""
        return _PowerBlade_Utils_swig.ByteToPseudoUARTi_sptr_set_processor_affinity(self, *args, **kwargs)

    def unset_processor_affinity(self):
        """unset_processor_affinity(ByteToPseudoUARTi_sptr self)"""
        return _PowerBlade_Utils_swig.ByteToPseudoUARTi_sptr_unset_processor_affinity(self)

    def processor_affinity(self):
        """processor_affinity(ByteToPseudoUARTi_sptr self) -> std::vector< int,std::allocator< int > >"""
        return _PowerBlade_Utils_swig.ByteToPseudoUARTi_sptr_processor_affinity(self)

    def active_thread_priority(self):
        """active_thread_priority(ByteToPseudoUARTi_sptr self) -> int"""
        return _PowerBlade_Utils_swig.ByteToPseudoUARTi_sptr_active_thread_priority(self)

    def thread_priority(self):
        """thread_priority(ByteToPseudoUARTi_sptr self) -> int"""
        return _PowerBlade_Utils_swig.ByteToPseudoUARTi_sptr_thread_priority(self)

    def set_thread_priority(self, *args, **kwargs):
        """set_thread_priority(ByteToPseudoUARTi_sptr self, int priority) -> int"""
        return _PowerBlade_Utils_swig.ByteToPseudoUARTi_sptr_set_thread_priority(self, *args, **kwargs)

    def name(self):
        """name(ByteToPseudoUARTi_sptr self) -> std::string"""
        return _PowerBlade_Utils_swig.ByteToPseudoUARTi_sptr_name(self)

    def symbol_name(self):
        """symbol_name(ByteToPseudoUARTi_sptr self) -> std::string"""
        return _PowerBlade_Utils_swig.ByteToPseudoUARTi_sptr_symbol_name(self)

    def input_signature(self):
        """input_signature(ByteToPseudoUARTi_sptr self) -> io_signature_sptr"""
        return _PowerBlade_Utils_swig.ByteToPseudoUARTi_sptr_input_signature(self)

    def output_signature(self):
        """output_signature(ByteToPseudoUARTi_sptr self) -> io_signature_sptr"""
        return _PowerBlade_Utils_swig.ByteToPseudoUARTi_sptr_output_signature(self)

    def unique_id(self):
        """unique_id(ByteToPseudoUARTi_sptr self) -> long"""
        return _PowerBlade_Utils_swig.ByteToPseudoUARTi_sptr_unique_id(self)

    def to_basic_block(self):
        """to_basic_block(ByteToPseudoUARTi_sptr self) -> basic_block_sptr"""
        return _PowerBlade_Utils_swig.ByteToPseudoUARTi_sptr_to_basic_block(self)

    def check_topology(self, *args, **kwargs):
        """check_topology(ByteToPseudoUARTi_sptr self, int ninputs, int noutputs) -> bool"""
        return _PowerBlade_Utils_swig.ByteToPseudoUARTi_sptr_check_topology(self, *args, **kwargs)

    def alias(self):
        """alias(ByteToPseudoUARTi_sptr self) -> std::string"""
        return _PowerBlade_Utils_swig.ByteToPseudoUARTi_sptr_alias(self)

    def set_block_alias(self, *args, **kwargs):
        """set_block_alias(ByteToPseudoUARTi_sptr self, std::string name)"""
        return _PowerBlade_Utils_swig.ByteToPseudoUARTi_sptr_set_block_alias(self, *args, **kwargs)

    def _post(self, *args, **kwargs):
        """_post(ByteToPseudoUARTi_sptr self, swig_int_ptr which_port, swig_int_ptr msg)"""
        return _PowerBlade_Utils_swig.ByteToPseudoUARTi_sptr__post(self, *args, **kwargs)

    def message_ports_in(self):
        """message_ports_in(ByteToPseudoUARTi_sptr self) -> swig_int_ptr"""
        return _PowerBlade_Utils_swig.ByteToPseudoUARTi_sptr_message_ports_in(self)

    def message_ports_out(self):
        """message_ports_out(ByteToPseudoUARTi_sptr self) -> swig_int_ptr"""
        return _PowerBlade_Utils_swig.ByteToPseudoUARTi_sptr_message_ports_out(self)

    def message_subscribers(self, *args, **kwargs):
        """message_subscribers(ByteToPseudoUARTi_sptr self, swig_int_ptr which_port) -> swig_int_ptr"""
        return _PowerBlade_Utils_swig.ByteToPseudoUARTi_sptr_message_subscribers(self, *args, **kwargs)

ByteToPseudoUARTi_sptr_swigregister = _PowerBlade_Utils_swig.ByteToPseudoUARTi_sptr_swigregister
ByteToPseudoUARTi_sptr_swigregister(ByteToPseudoUARTi_sptr)

ByteToPseudoUARTi_sptr.__repr__ = lambda self: "<gr_block %s (%d)>" % (self.name(), self.unique_id())
ByteToPseudoUARTi = ByteToPseudoUARTi.make;


